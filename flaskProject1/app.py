from flask import Flask, render_template
import pandas as pd
import plotly.graph_objs as go

app = Flask(__name__, static_folder='static')  # Specify the static folder

# Load your CSV file globally
df = pd.read_csv('historical_data.csv')

@app.route('/')
def index():
    if df is not None:
        # Filter data for trading code 'BATBC'
        batbc_df = df[df['trading_code'] == 'BATBC']

        # Create a Plotly figure
        fig = go.Figure()

        # Plot opening price using the index as the x-axis
        fig.add_trace(go.Scatter(x=batbc_df.index, y=batbc_df['opening_price'], mode='lines', name='Opening Price'))

        # Plot closing price using the index as the x-axis
        fig.add_trace(go.Scatter(x=batbc_df.index, y=batbc_df['closing_price'], mode='lines', name='Closing Price'))

        fig.update_layout(title='BATBC Opening and Closing Prices', xaxis_title='Index', yaxis_title='Price')

        # Convert the Plotly figure to JSON
        graphJSON = fig.to_json()

        # Pass the JSON data to the template
        return render_template('index.html', graphJSON=graphJSON)
    else:
        return "Failed to load CSV file. Please check the file path and format."

if __name__ == '__main__':
    app.run(debug=True)
