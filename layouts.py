import dash_core_components as dcc
import dash_html_components as html
from data_reader import data, data_pred, active_customer, total_customer, expected_monthly_income, churn_rate

from data_reader import pred_churn_list,pred_churn_count_percent,pred_churn_list_true
import dash_table

from graphs import *


def no_with_comma(n):
    return "{:,}".format(n)


def no_to_percentage(n):
    return "{0:.2f}%".format(n)


# For individual boxes at top like total active cases, recovered etc.
mini_container_style = {
    'border-radius': '10px',
    'background-color': '#f9f9f9',
    'margin-left': '40px',
    'margin-right': '40px',
    'padding': '0%',
    'position': 'relative',
    # 'box-shadow': '2px 2px 2px lightgrey',
    'width': '25%',
    'border-style': 'solid',
    'border-width': '2px',
    'border-color': 'black'
}

tab2_mini_container_style = {
    'border-radius': '10px',
    'background-color': '#f9f9f9',
    'margin-left': '40px',
    'margin-right': '40px',
    'padding': '0%',
    'position': 'relative',
    # 'box-shadow': '2px 2px 2px lightgrey',
    'width': '50%',
    'border-style': 'solid',
    'border-width': '2px',
    'border-color': 'black'
}

# For div containg above boxex
whole_container = {'display': 'flex',
                   'text-align': 'center',
                   }

tab_style = {

    'fontWeight': 'bold',
    'font-size': '22px'
}

tab_selected_style = {
    'fontWeight': 'bold',
    'font-size': '22px'
}



def two_tab_layout():
    return html.Div([
        dcc.Tabs(id='tabs-example', value='tab-1', children=[
            dcc.Tab(label='Home Tab', value='tab-1', style=tab_style, selected_style=tab_selected_style, children=[
                    html.Br(),
                    html.Br(),
                    html.H1(children="Churn Analysis-Dashboard",
                            style={'color': 'black', 'textAlign': 'center'}),

                    html.Div([
                        html.Div([
                            html.Div([html.P(html.B("Active Customer", style={'font-size': '25px'})), html.P(
                                no_with_comma(active_customer), style={'font-size': '22px'})], style=mini_container_style),
                            #html.Div([html.P("<b>Active Customer</b>"),html.P(no_with_comma(active_customer))],style = mini_container_style),
                            html.Div([html.P(html.B("Total Customer", style={'font-size': '25px'})), html.P(
                                no_with_comma(total_customer), style={'font-size': '22px'})], style=mini_container_style),
                            html.Div([html.P(html.B("Churn Rate", style={'font-size': '25px'})), html.P(
                                no_to_percentage(churn_rate), style={'font-size': '22px'})], style=mini_container_style),
                            html.Div([html.P(html.B("Monthly revenue", style={'font-size': '25px'})), html.P(no_with_comma(
                                expected_monthly_income), style={'font-size': '22px'})], style=mini_container_style),

                        ], style=whole_container)
                    ], className='row'),


                    html.Div(children=[

                        html.Div([
                            html.Div(children=[
                                dcc.Graph(id="bar-graph2", figure=fig5,
                                          style={'display': 'inline-block','width':'50%','text-align': 'center'}),
                                dcc.Graph(id="bar-graph3", figure=fig3,
                                          style={'display': 'inline-block', 'width': '50%'})
                            ], style={'display': 'flex'})
                        ]),

                        html.Div([
                            dcc.Graph(id="bar-graph1", figure=fig),
                        ]),


                        html.Div([
                            html.Div(children=[
                                dcc.Graph(id="bar-graph4", figure=fig2,
                                          style={'display': 'inline-block', 'width': '50%'}),
                                dcc.Graph(id="bar-graph5", figure=fig4,
                                          style={'display': 'inline-block', 'width': '50%'})
                            ], style={'display': 'flex'})
                        ])
                    ])
                    ]),


            # churn predictions tab


            dcc.Tab(label='Churn Predictions', value='tab-2', style=tab_style, selected_style=tab_selected_style, children=[

                 html.Br(),
                    html.Br(),
                    html.H1(children="Churn Predictions",
                            style={'color': 'black', 'textAlign': 'center'}),

                    html.Div([
                        html.Div([
                            html.Div([html.P(html.B("Predicted Churn Count %", style={'font-size': '25px'})), html.P(
                             no_to_percentage(pred_churn_count_percent), style={'font-size': '22px'})], style=tab2_mini_container_style),

                            html.Div([html.P(html.B("Predicted Churn Count", style={'font-size': '25px'})), html.P(
                                no_with_comma(pred_churn_list_true), style={'font-size': '22px'})], style=tab2_mini_container_style),

                        ], style=whole_container)
                    ], className='row'),

                    html.Br(),
                    html.Br(),

                    html.Div([
                        dcc.Dropdown(
                            id='dropdown-table',
                            options=[
                                {'label': 'Train Data', 'value': 'train'},
                                {'label': 'Predicted Results', 'value': 'pred_res'},
                                {'label': 'Test Data', 'value': 'test'}
                                
                            ],
                            value='train'
                        ),
                        
                    ]),

                    # html.Div(id='dd-output-container'),
                    html.Br(),
                    html.Br(),

                    html.Div(id='table-div')
                   
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

                    ]),
        ]),
        # html.Div(id='tabs-example-content')
    ])


