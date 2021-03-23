import dash_core_components as dcc
import dash_html_components as html
from data_reader import *
import dash_table

from graphs import *


def no_with_comma(n):
    return "{:,}".format(n)


def no_to_percentage(n):
    return "{0:.2f}%".format(n)


# For individual boxes at top like total active cases, recovered etc.
mini_container_style = {
    "border-radius": "10px",
    "background-color": "#f9f9f9",
    "margin-left": "40px",
    "margin-right": "40px",
    "padding": "0%",
    "position": "relative",
    # 'box-shadow': '2px 2px 2px lightgrey',
    "width": "25%",
    "border-style": "solid",
    "border-width": "2px",
    "border-color": "black",
}

tab2_mini_container_style = {
    "border-radius": "10px",
    "background-color": "#f9f9f9",
    "margin-left": "40px",
    "margin-right": "40px",
    "padding": "0%",
    "position": "relative",
    # 'box-shadow': '2px 2px 2px lightgrey',
    "width": "50%",
    "border-style": "solid",
    "border-width": "2px",
    "border-color": "black",
}

# For div containg above boxex
whole_container = {
    "display": "flex",
    "text-align": "center",
}

tab_style = {"fontWeight": "bold", "font-size": "22px"}

tab_selected_style = {"fontWeight": "bold", "font-size": "22px"}


def home_tab_layout():
    return html.Div(
        [
            html.Br(),
            html.Br(),
            html.H1(
                children="Churn Analysis-Dashboard",
                style={"color": "black", "textAlign": "center"},
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.P(
                                        html.B(
                                            "Active Customer",
                                            style={"font-size": "25px"},
                                        )
                                    ),
                                    html.P(
                                        no_with_comma(active_customer),
                                        style={"font-size": "22px"},
                                    ),
                                ],
                                style=mini_container_style,
                            ),
                            # html.Div([html.P("<b>Active Customer</b>"),html.P(no_with_comma(active_customer))],style = mini_container_style),
                            html.Div(
                                [
                                    html.P(
                                        html.B(
                                            "Total Customer",
                                            style={"font-size": "25px"},
                                        )
                                    ),
                                    html.P(
                                        no_with_comma(total_customer),
                                        style={"font-size": "22px"},
                                    ),
                                ],
                                style=mini_container_style,
                            ),
                            html.Div(
                                [
                                    html.P(
                                        html.B(
                                            "Churn Rate", style={"font-size": "25px"}
                                        )
                                    ),
                                    html.P(
                                        no_to_percentage(churn_rate),
                                        style={"font-size": "22px"},
                                    ),
                                ],
                                style=mini_container_style,
                            ),
                            html.Div(
                                [
                                    html.P(
                                        html.B(
                                            "Monthly revenue",
                                            style={"font-size": "25px"},
                                        )
                                    ),
                                    html.P(
                                        no_with_comma(expected_monthly_income),
                                        style={"font-size": "22px"},
                                    ),
                                ],
                                style=mini_container_style,
                            ),
                        ],
                        style=whole_container,
                    )
                ],
                className="row",
            ),
            html.Div(
                children=[
                    html.Div(
                        [
                            html.Div(
                                children=[
                                    dcc.Graph(
                                        id="bar-graph2",
                                        figure=fig5,
                                        style={
                                            "display": "inline-block",
                                            "width": "50%",
                                            "text-align": "center",
                                        },
                                    ),
                                    dcc.Graph(
                                        id="bar-graph3",
                                        figure=fig3,
                                        style={
                                            "display": "inline-block",
                                            "width": "50%",
                                        },
                                    ),
                                ],
                                style={"display": "flex"},
                            )
                        ]
                    ),
                    html.Div(
                        [
                            dcc.Graph(id="bar-graph1", figure=fig),
                        ]
                    ),
                    html.Div(
                        [
                            html.Div(
                                children=[
                                    dcc.Graph(
                                        id="bar-graph4",
                                        figure=fig2,
                                        style={
                                            "display": "inline-block",
                                            "width": "50%",
                                        },
                                    ),
                                    dcc.Graph(
                                        id="bar-graph5",
                                        figure=fig4,
                                        style={
                                            "display": "inline-block",
                                            "width": "50%",
                                        },
                                    ),
                                ],
                                style={"display": "flex"},
                            )
                        ]
                    ),
                ]
            ),
        ]
    )


def churn_data_tab():
    return html.Div(
        [
            html.Br(),
            html.Br(),
            html.H1(
                children="Churn Data", style={"color": "black", "textAlign": "center"}
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.P(
                                        html.B(
                                            "Predicted Churn Count %",
                                            style={"font-size": "25px"},
                                        )
                                    ),
                                    html.P(
                                        no_to_percentage(pred_churn_count_percent),
                                        style={"font-size": "22px"},
                                    ),
                                ],
                                style=tab2_mini_container_style,
                            ),
                            html.Div(
                                [
                                    html.P(
                                        html.B(
                                            "Predicted Churn Count",
                                            style={"font-size": "25px"},
                                        )
                                    ),
                                    html.P(
                                        no_with_comma(pred_churn_list_true),
                                        style={"font-size": "22px"},
                                    ),
                                ],
                                style=tab2_mini_container_style,
                            ),
                        ],
                        style=whole_container,
                    )
                ],
                className="row",
            ),
            html.Br(),
            html.H6(
                children=["Select Dataset to be Displayed"],
                style={"text-align": "center"},
            ),
            html.Div(
                [
                    dcc.Dropdown(
                        id="dropdown-table",
                        options=[
                            {"label": "Train Data", "value": "train"},
                            {"label": "Predicted Results", "value": "pred_res"},
                            {"label": "Test Data", "value": "test"},
                            {"label": "Churn Customers", "value": "churn_cust"},
                            {"label": "Churn Changes", "value": "churn_changes"},
                        ],
                        value="pred_res",
                    ),
                ]
            ),
            # html.Div(id='dd-output-container'),
            html.Br(),
            html.H6(
                children=["Select Columns to Display In table"],
                style={"text-align": "center"},
            ),
            html.Div(
                [
                    dcc.Dropdown(
                        id="dropdown-column-select",
                        options=[],
                        multi=True,
                    )
                ]
            ),
            html.Br(),
            html.Br(),
            html.Div(id="table-div")
            # html.Div([
            #     dash_table.DataTable(
            #         id='table',
            #         columns=[{"name": i, "id": i}
            #                  for i in data_pred.columns],
            #         data=data_pred.to_dict('records'),
            #         page_size=15,
            #         fixed_rows={'headers': True},
            #     )
            # ]),
        ]
    )


# def serve_roc_curve():
#     fpr, tpr, threshold = roc_curve(df_churn, preds)
#     auc_score = roc_auc_score(y_true=df_churn, y_score=preds)

#     trace0 = go.Scatter(
#         x=fpr, y=tpr, mode="lines", name="Test Data", marker={"color": "#13c6e9"}
#     )

#     layout = go.Layout(
#         title=f"ROC Curve (AUC = {auc_score:.3f})",
#         xaxis=dict(title="False Positive Rate", gridcolor="#2f3445"),
#         yaxis=dict(title="True Positive Rate", gridcolor="#2f3445"),
#         legend=dict(x=0, y=1.05, orientation="h"),
#         margin=dict(l=100, r=10, t=25, b=40),
#         plot_bgcolor="#282b38",
#         paper_bgcolor="#282b38",
#         font={"color": "#a5b1cd"},
#     )

#     data0 = [trace0]
#     figure = go.Figure(data=data0, layout=layout)

#     return figure


def serve_pie_confusion_matrix():
    # Compute threshold
    #     scaled_threshold = threshold * (Z.max() - Z.min()) + Z.min()
    #     y_pred_test = (model.decision_function(X_test) > scaled_threshold).astype(int)

    matrix = confusion_matrix(y_true=df_churn, y_pred=preds)
    tn, fp, fn, tp = matrix.ravel()

    values = [tp, fn, fp, tn]
    label_text = ["True Positive", "False Negative",
                  "False Positive", "True Negative"]
    labels = ["TP", "FN", "FP", "TN"]
    blue = cl.flipper()["seq"]["9"]["Blues"]
    red = cl.flipper()["seq"]["9"]["Reds"]
    colors = ["#13c6e9", blue[1], "#ff916d", "#ff744c"]

    trace0 = go.Pie(
        labels=label_text,
        values=values,
        hoverinfo="label+value+percent",
        textinfo="text+value",
        text=labels,
        sort=False,
        marker=dict(colors=colors),
        insidetextfont={"color": "white"},
        rotation=90,
    )

    layout = go.Layout(
        title="Confusion Matrix",
        margin=dict(l=50, r=50, t=100, b=10),
        legend=dict(bgcolor="#282b38", font={
                    "color": "#a5b1cd"}, orientation="h"),
        plot_bgcolor="#282b38",
        paper_bgcolor="#282b38",
        font={"color": "#a5b1cd"},
    )

    train_data_X_pred_xgb01_70acc = [trace0]
    figure = go.Figure(data=data0, layout=layout)

    return figure

def churn_model_tab_layout():

    # roc_figure = serve_roc_curve()

    # confusion_figure = serve_pie_confusion_matrix()


    return html.Div([
            html.Br(),
            html.Br(),
            
            html.H6(
                children=["Select ML model"],
                style={"text-align": "center"},
            ),

            dcc.Dropdown(
                    id='model-select-dropdown',
                    options=[
                        {'label': 'xgboost', 'value': 'xgboost'},
                    ],
                    value='xgboost',
                    clearable=False,
                    ),
            
            html.Div(
                id="graphs-container",
                children=[
                    # dcc.Loading(
                    #     className="graph-wrapper",
                    #     children=dcc.Graph(id="graph-line-roc-curve",figure=roc_figure)
                    # ), 
                    # dcc.Loading(
                    #     className="graph-wrapper",
                    #     children=dcc.Graph(
                    #         id="graph-pie-confusion-matrix", figure=confusion_figure
                    #     ),
                    # ),
                ]
            )
            
       



        ])
  
  


def tab_layout():
    return html.Div(
        [
            dcc.Tabs(
                id="tabs-example",
                value="tab-1",
                children=[
                    # Home Tab
                    dcc.Tab(
                        label="Home Tab",
                        value="tab-1",
                        style=tab_style,
                        selected_style=tab_selected_style,
                        children=[home_tab_layout()],
                    ),
                    # Churn Predictions tab
                    dcc.Tab(
                        label="Churn Data",
                        value="tab-2",
                        style=tab_style,
                        selected_style=tab_selected_style,
                        children=[churn_data_tab()],
                    ),
                    # Churn Model Tab
                    dcc.Tab(
                        label="Churn Model",
                        value="tab-3",
                        style=tab_style,
                        selected_style=tab_selected_style,
                        children=[
                            churn_model_tab_layout()
                            ],
                    ),
                ],
            ),
        ]
    )
