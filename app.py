

import dash
import dash_auth

import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
from data_reader import data


from layouts import home_layout,two_tab_layout
from  callbacks import *

#colour = ["#290934", "#40204a", "#583861", "#705079", "#896a91"]
#colour = ["#8a0e4a", "#9a305c", "#a9496e", "#b86181", "#c67894"]


VALID_USERNAME_PASSWORD_PAIRS = {
    'admin': 'admin'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

server = app.server



app.layout = two_tab_layout()


# @app.callback(Output('tabs-example-content', 'children'),
#               Input('tabs-example', 'value'))
# def render_content(tab):
#     if tab == 'tab-1':
#         return html.Div([
            
#         ])
#     elif tab == 'tab-2':
#         return html.Div([
#             # html.H3('Churn Predictions')
#         ])


if __name__ == '__main__':
    app.run_server(debug=False)
