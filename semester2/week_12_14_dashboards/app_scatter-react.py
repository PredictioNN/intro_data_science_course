# source: https://dash.plotly.com/layout

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('C:/Users/apt4c/Documents/repos/covenant_ds/semester2/datasets/Country_Happiness.csv')

fig = px.scatter(df, x="Explained by: GDP per capita", y="Happiness score",
                 hover_name="Country",
                 log_x=True, size_max=60)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='happiness-vs-gdp',
        figure=fig
    ),
    dcc.Dropdown(df.Country.sort_values(), 'Norway', id='demo-dropdown'),
    html.Div(id='dd-output-container')
])

@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    return f'You have selected {value}'

if __name__ == '__main__':
    app.run_server(debug=True)