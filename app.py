# # import dash
# from dash import Dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import plotly.express as px
# import pandas as pd

# df = pd.read_csv('dth_data_1.csv')

# app = Dash()    
# server = app.server  

# #server = app.server

# app.layout = html.Div([

#     html.H1(children='Churn Analysis G22'),
#     html.Div(children='''
#         Dashboard
#     '''),
#     dcc.Graph(id="graph"),
#     html.Button("Switch Axis", id='btn', n_clicks=0)
# ])

# @app.callback(
#     Output("graph", "figure"), 
#     [Input("btn", "n_clicks")])
# def display_graph(n_clicks):
#     if n_clicks % 2 == 0:
#         x, y =  'dth_pack_price', 'no_of_channels'
#     else:
#         x, y = 'dth_pack_price', 'no_of_channels'
#     fig = px.line(df, x=x, y=y)    
#     return fig



# if __name__ == '__main__':
#    app.run_server(debug=True)
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:20:07 2021

@author: admin
"""


import dash
import dash_auth
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go   #for scatter graph
import pandas as pd
import seaborn as sns

data = pd.read_csv("dth_data_1.csv")

ott_subs = dict(data.ott_subscription.value_counts())
fig = px.bar(x=list(ott_subs.keys()), y=list(ott_subs.values()), title="Popularity of OTT Platform ")

dth_pack = dict(data.dth_pack.value_counts())
fig2 = px.bar(x=list(dth_pack.keys()), y=list(dth_pack.values()), title="DTH Pack distribution")

sub_status = dict(data.subscription_status.value_counts())
fig3 = px.bar(x=list(sub_status.keys()), y=list(sub_status.values()), title="Subscription status")

cust_class = dict(data.customer_class.value_counts())
fig4 = px.bar(x=list(cust_class.keys()), y=list(cust_class.values()), title="Customer class")

churn = dict(data.churn.value_counts())
fig5 = px.bar(x=list(churn.keys()), y=list(churn.values()), title="Churn")


VALID_USERNAME_PASSWORD_PAIRS = {
    'admin': 'admin'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

#For individual boxes at top like total active cases, recovered etc.
mini_container_style = {
    'border-radius': '10px',
    'background-color': '#f9f9f9',
    'margin-left': '40px',
    'margin-right': '40px',
    'padding': '0%',
    'position': 'relative',
    #'box-shadow': '2px 2px 2px lightgrey',
    'width':'25%',
    'border-style': 'solid',
    'border-width': '2px',
    'border-color': 'black'
    }

    #For div containg above boxex
whole_container = {'display': 'flex', 'text-align': 'center'}


app.layout = html.Div(className='row', children=[
   html.H1(children = "Churn Analysis-Dashboard", style = {'color':'black', 'textAlign': 'center'}),
   
   html.Div([
                 html.Div([
                    html.Div([html.P("Active Customer"),html.P('1')],style = mini_container_style),
                    html.Div([html.P("Total Customer "),html.P('2')],style = mini_container_style),
                    html.Div([html.P("Churn Rate"),html.P('3')],style = mini_container_style),
                    html.Div([html.P("Expected Monthly revenue"),html.P('4')],style = mini_container_style),
                    
                         ], style = whole_container)
                ], className='row'),
   
   
   html.Div(children=[
       html.Div([
           dcc.Graph(id = "bar-graph1", figure = fig),
           ]),
       
       html.Div([
           html.Div(children=[
               dcc.Graph(id = "bar-graph2", figure = fig2, style={'display': 'inline-block'}), 
               dcc.Graph(id = "bar-graph3", figure = fig3, style={'display': 'inline-block'})
    ], style = {'display': 'flex'})
           ]),
       html.Div([
           html.Div(children=[
               dcc.Graph(id = "bar-graph4", figure = fig4, style={'display': 'inline-block'}), 
               dcc.Graph(id = "bar-graph5", figure = fig5, style={'display': 'inline-block'})
    ], style = {'display': 'flex'})
           ])
    ])
])


if __name__ == '__main__':
    app.run_server(debug=False)
