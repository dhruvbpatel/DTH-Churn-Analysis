
import plotly.express as px
import plotly.graph_objects as go

from Sentiment import *
from data_reader import *
import pandas as pd

from layouts import tab_layout
import dash_table
import dash
import dash_auth

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output



# colour = ["#290934", "#40204a", "#583861", "#705079", "#896a91"]
# colour = ["#8a0e4a", "#9a305c", "#a9496e", "#b86181", "#c67894"]



VALID_USERNAME_PASSWORD_PAIRS = {"admin": "admin"}


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)

server = app.server


app.layout = tab_layout()


## callbacks


## callbacks

# @app.callback(
#     Output('table-div', 'children'),
#     Input('dropdown-table', 'value')
# )
# def update_datatable(value):
#     if value == 'train':
#         dframe = data
#     elif value == 'test':
#         dframe = test_data
#     else:
#         dframe = data_pred

#     return dash_table.DataTable(
#         id='table',

#         columns=[{"name": i, "id": i}
#                  for i in dframe.columns],
#         data=dframe.to_dict('records'),
#         page_size=15,
#         fixed_rows={'headers': True},

#     )


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


## tab layout callback
@app.callback(
    Output("tabs-example-content", "children"), Input("tabs-example", "value")
)
def render_content(tab):
    if tab == "tab-1":
        return html.Div([])
    elif tab == "tab-2":
        return html.Div(
            [
                # html.H3('Churn Predictions')
            ]
        )


## dropdown callback - churn prediction tab
# @app.callback(
#     Output('table-div', 'children'),
#     Input('dropdown-table', 'value')
# )
# def update_datatable(value):

#     if value == 'train':
#         dframe = data
#     elif value == 'test':
#         dframe = test_data
#     elif value == 'pred_res':
#         dframe = data_pred
#     elif value == 'churn_cust':
#         dframe = data_pred[data_pred['pred_churn']==1]
#     elif value == 'churn_changes':
#         dframe = pred_changes

#     return dash_table.DataTable(
#         id='table',
#         columns=[{"name": i, "id": i}
#                  for i in dframe.columns],
#         data=dframe.to_dict('records'),
#         page_size=15,
#         fixed_rows={'headers': True},

#         style_header={
#             'backgroundColor': 'rgb(230, 230, 230)',
#             'fontWeight': 'bold'
#         },
#     )

## multi select dropdown column
@app.callback(
    Output("dropdown-column-select", "options"),
    Input("dropdown-table", "value"),
)
def dropdown_columns(value):
    if value == "train":
        dframe = data
    elif value == "test":
        dframe = test_data
    elif value == "pred_res":
        dframe = data_pred
    elif value == "churn_cust":
        dframe = data_pred[data_pred["pred_churn"] == 1]
    elif value == "churn_changes":
        dframe = pred_changes

    options = []
    for col in dframe:
        options.append({"label": "{}".format(col, col), "value": col})

    return options


## update table according to multi select dropdown column


@app.callback(
    Output("table-div", "children"),
    Input("dropdown-table", "value"),
    Input("dropdown-column-select", "value"),
)
def update_datatable_column(data_value, col_value):

    if data_value == "train":
        dframe = data
    elif data_value == "test":
        dframe = test_data
    elif data_value == "pred_res":
        dframe = data_pred
    elif data_value == "churn_cust":
        dframe = data_pred[data_pred["pred_churn"] == 1]
    elif data_value == "churn_changes":
        dframe = pred_changes

    if col_value:
        dframe = pd.DataFrame(dframe[col_value])

    return dash_table.DataTable(
        id="table",
        columns=[{"name": i, "id": i} for i in dframe.columns],
        data=dframe.to_dict("records"),
        page_size=15,
        fixed_rows={"headers": True},
        filter_action="native",
        style_header={"backgroundColor": "rgb(230, 230, 230)", "fontWeight": "bold"},
        style_table={"height": 400},
        style_data={
            "width": "{}%".format(100.0 / len(dframe.columns)),
            "textOverflow": "hidden",
        }
        # css=[{
        #     'selector': 'table',
        #     'rule': 'table-layout: fixed'  # note - this does not work with fixed_rows
        # }],
        ,
        style_cell={"min-width": "100px"},
        css=[{"selector": ".row-1", "rule": "min-height: 500px;"}],
    )

@app.callback(
    Output("table-div_r", "children"),
    Input("dropdown-table1", "value"),
)
def dropdown_columns_sentiment(value):
    dframe = pred_sentiment
    if value == "positive_r":
        dframe = dframe[dframe["Predicted_Sentiment"]=="Positive"]
    elif value == "negative_r":
        dframe = dframe[dframe["Predicted_Sentiment"]=="Negative"]
    elif value == "neutral_r":
        dframe = dframe[dframe["Predicted_Sentiment"]=="Neutral"]

    # options = []
    # for col in dframe:
    #     options.append({"label": "{}".format(col, col), "value": col})
    # if col_value:
    #     dframe = pd.DataFrame(dframe[col_value])

    return dash_table.DataTable(
        id="table2",
        columns=[{"name": i, "id": i} for i in dframe.columns],
        data=dframe.to_dict("records"),
        page_size=15,
        fixed_rows={"headers": True},
        filter_action="native",
        style_header={"backgroundColor": "rgb(230, 230, 230)", "fontWeight": "bold"},
        style_table={"height": 400},
        style_data={
            "width": "{}%".format(100.0 / len(dframe.columns)),
            "textOverflow": "hidden",
        }
        # css=[{
        #     'selector': 'table',
        #     'rule': 'table-layout: fixed'  # note - this does not work with fixed_rows
        # }],
        ,
        style_cell={"min-width": "100px"},
        css=[{"selector": ".row-1", "rule": "min-height: 500px;"}],
    )

    

if __name__ == "__main__":
    app.run_server(debug=False, port=8051)
