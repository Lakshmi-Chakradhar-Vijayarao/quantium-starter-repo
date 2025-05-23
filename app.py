import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load the processed sales data
df = pd.read_csv('processed/pink_morsel_sales.csv')

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Aggregate total sales by date (summing across regions)
df_daily = df.groupby('date', as_index=False)['Sales'].sum()

# Sort by date to ensure correct plotting order
df_daily = df_daily.sort_values('date')

# Initialize Dash app
app = Dash(__name__)

# Create line chart using Plotly Express
fig = px.line(
    df_daily,
    x='date',
    y='Sales',
    title='Pink Morsel Sales Over Time',
    labels={'date': 'Date', 'Sales': 'Total Sales ($)'}
)

# Dash app layout
app.layout = html.Div(children=[
    html.H1('Pink Morsel Sales Visualiser'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)
