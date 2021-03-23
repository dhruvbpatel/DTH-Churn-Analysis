# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:11:22 2021

@author: admin
"""

# g=sns.heatmap(df.corr(),cmap="RdYlGn",annot=True)
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("D:\github repo\DTH-Churn-Analysis\dth_data_1.csv")

corr = df.corr()

# ff.create_annotated_heatmap()

fig = go.Figure(
    data=go.Heatmap(z=corr.values, x=corr.index.values, y=corr.columns.values)
)


import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(
    [
        html.Div(
            children=[
                dcc.Graph(figure=fig, style={"display": "inline-block", "width": "50%"})
            ]
        )
    ]
)

app.run_server(debug=True, use_reloader=False)
