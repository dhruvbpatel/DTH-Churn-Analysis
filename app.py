
import dash
import dash_auth

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
from data_reader import data, data_pred


from layouts import two_tab_layout
import dash_table
from data_reader import *


# from  callbacks import *

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


## callbacks

## dropdown callback - churn prediction tab

@app.callback(
    Output('table-div', 'children'),
    Input('dropdown-table', 'value')
)
def update_datatable(value):
   

    if value == 'train':
        dframe = data
    elif value == 'test':
        dframe = test_data
    elif value == 'pred_res':
        dframe = data_pred
    elif value == 'churn_cust':
        dframe = data_pred[data_pred['pred_churn']==1]
    elif value == 'churn_changes':
        dframe = pred_changes

    return dash_table.DataTable(
        id='table',

        columns=[{"name": i, "id": i}
                 for i in dframe.columns],
        data=dframe.to_dict('records'),
        page_size=15,
        # fixed_rows={'headers': True},
        
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        },

        # style_header_conditional=[
        #     {
        #         'if':{
        #             'filter_query':{churn}==True,
        #             'column_id=':'churn'
        #         },
        #         'color':'red',
        #         'fontWeight':'bold'
        #     }
        # ]

    )

## tab layout callback
@app.callback(Output('tabs-example-content', 'children'),
              Input('tabs-example', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([

        ])
    elif tab == 'tab-2':
        return html.Div([
            # html.H3('Churn Predictions')
        ])


if __name__ == '__main__':
    app.run_server(debug=False)
