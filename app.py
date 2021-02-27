# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:20:07 2021

@author: admin
"""


import dash
import dash_auth
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd

def no_with_comma(n):
    return "{:,}".format(n)
def no_to_percentage(n):
    return "{0:.2f}%".format(n)


data = pd.read_csv("dth_data_1.csv")

colour = ["#003f5c", "#396582", "#668eaa", "#93bad4", "#c2e7ff"]

#colour = ["#290934", "#40204a", "#583861", "#705079", "#896a91"]
#colour = ["#8a0e4a", "#9a305c", "#a9496e", "#b86181", "#c67894"]


ott_subs = dict(data.ott_subscription.value_counts())
fig = px.bar(x=list(ott_subs.keys()), y=list(ott_subs.values()), color=colour, color_discrete_map="identity", title="<b>Popularity of OTT Platform</b>", 
             labels={'x':'OTT Platforms', 'y':'Number of users'}
             )

dth_pack = dict(data.dth_pack.value_counts())
fig2 = px.bar(x=list(dth_pack.keys()), y=list(dth_pack.values()), color=colour[:3], color_discrete_map="identity", title="<b>DTH Pack distribution</b>",
              labels={'x':'DTH Pack Type', 'y':'Number of users'}
              )

'''sub_status = dict(data.subscription_status.value_counts())
fig3 = px.bar(x=list(sub_status.keys()), y=list(sub_status.values()), title="Subscription status")'''

sub_status = dict(data.subscription_status.value_counts())
#fig3 = px.pie(values=list(sub_status.values()), names=list(sub_status.keys()),color_discrete_sequence= ["#003f5c", "#668eaa"], title="<b>Subscription status</b>",)
fig3 = go.Figure(data=[go.Pie(labels=list(sub_status.keys()), values=list(sub_status.values()), pull=[0, 0.1])])
fig3.update_layout(title_text="<b>Subscription status</b>")
fig3.update_traces(marker=dict(colors=["#003f5c", "#668eaa"]))

cust_class = dict(data.customer_class.value_counts())
fig4 = px.bar(x=list(cust_class.keys()), y=list(cust_class.values()),color=colour[:3], color_discrete_map="identity", title="<b>Customer class</b>",
              labels={'x':'Customer class', 'y':'Number of users'}
              )

churn = dict(data.churn.value_counts())
fig5 = px.bar(x=list(churn.keys()), y=list(churn.values()),color=colour[:2], color_discrete_map="identity", title="<b>Churn</b>",
              labels={'x':'Churn', 'y':'Number of users'}
              )

#Query to fetch data in dashboard 
active_customer = dict(data.subscription_status.value_counts())
active_customer = active_customer[True]

total_customer = len(data)

churn_rate = dict(data.churn.value_counts())
churn_rate = (churn_rate[True]/(churn_rate[False]+churn_rate[True]))*100

expected_monthly_income = data[data["subscription_status"]==True]["dth_pack_price"].sum()


VALID_USERNAME_PASSWORD_PAIRS = {
    'admin': 'admin'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

server = app.server


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
                    html.Div([html.P("Active Customer"),html.P(no_with_comma(active_customer))],style = mini_container_style),
                    html.Div([html.P("Total Customer "),html.P(no_with_comma(total_customer))],style = mini_container_style),
                    html.Div([html.P("Churn Rate"),html.P(no_to_percentage(churn_rate))],style = mini_container_style),
                    html.Div([html.P("Monthly revenue"),html.P(no_with_comma(expected_monthly_income))],style = mini_container_style),
                    
                         ], style = whole_container)
                ], className='row'),
   
   
   html.Div(children=[
       
       html.Div([
           html.Div(children=[
               dcc.Graph(id = "bar-graph2", figure = fig5, style={'display': 'inline-block'}), 
               dcc.Graph(id = "bar-graph3", figure = fig3, style={'display': 'inline-block'})
    ], style = {'display': 'flex'})
           ]),
       
       html.Div([
           dcc.Graph(id = "bar-graph1", figure = fig),
           ]),
       
       
       html.Div([
           html.Div(children=[
               dcc.Graph(id = "bar-graph4", figure = fig2, style={'display': 'inline-block'}), 
               dcc.Graph(id = "bar-graph5", figure = fig4, style={'display': 'inline-block'})
    ], style = {'display': 'flex'})
           ])
    ])
])


if __name__ == '__main__':
    app.run_server(debug=False)



