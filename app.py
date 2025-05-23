import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load the processed data
df = pd.read_csv('processed/pink_morsel_sales.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualizer"),
    
    # Radio buttons for region selection
    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
        ],
        value='all',
        labelStyle={'display': 'inline-block', 'margin-right': '15px'}
    ),
    
    dcc.Graph(id='sales-line-chart'),
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_line_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'].str.lower() == selected_region]
    
    # Group by date and sum sales for the line chart
    grouped = filtered_df.groupby('date', as_index=False)['Sales'].sum()
    
    fig = px.line(grouped, x='date', y='Sales', title=f'Sales over Time - {selected_region.capitalize()} Region')
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':
    app.run(debug=True)

