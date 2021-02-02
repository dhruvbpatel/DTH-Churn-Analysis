# import dash
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('dth_data_1.csv')

app = Dash()    
server = app.server  

#server = app.server

app.layout = html.Div([

    html.H1(children='Churn Analysis G22'),
    html.Div(children='''
        Dashboard
    '''),
    dcc.Graph(id="graph"),
    html.Button("Switch Axis", id='btn', n_clicks=0)
])

@app.callback(
    Output("graph", "figure"), 
    [Input("btn", "n_clicks")])
def display_graph(n_clicks):
    if n_clicks % 2 == 0:
        x, y =  'dth_pack_price', 'no_of_channels'
    else:
        x, y = 'dth_pack_price', 'no_of_channels'
    fig = px.line(df, x=x, y=y)    
    return fig



if __name__ == '__main__':
   app.run_server(debug=True)