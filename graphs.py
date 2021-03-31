import plotly.express as px
import plotly.graph_objects as go
from data_reader import *
import colorlover as cl

from sklearn.metrics import (
    accuracy_score,
    r2_score,
    confusion_matrix,
    plot_confusion_matrix,
    roc_auc_score,
    roc_curve,
)


colour = ["#2c3e50", "#e74c3c", "#bdc3c7", "#f39c12", "#7ccc63"]


ott_subs = dict(data.ott_subscription.value_counts())
fig = px.bar(
    x=list(ott_subs.keys()),
    y=list(ott_subs.values()),
    color=colour,
    color_discrete_map="identity",
    title="<b>Popularity of OTT Platform</b>",
    labels={"x": "OTT Platforms", "y": "Number of users"},
)

dth_pack = dict(data.dth_pack.value_counts())
"""fig2 = px.bar(x=list(dth_pack.keys()), y=list(dth_pack.values()), color=colour[:3], color_discrete_map="identity", title="<b>DTH Pack distribution</b>",
              labels={'x':'DTH Pack Type', 'y':'Number of users'}
              )"""

fig2 = go.Figure(
    data=[go.Pie(labels=list(dth_pack.keys()), values=list(dth_pack.values()))]
)
fig2.update_layout(title_text="<b> DTH Pack distribution </b>")
fig2.update_traces(marker=dict(colors=["#2c3e50", "#e74c3c", "#bdc3c7"]))

"""sub_status = dict(data.subscription_status.value_counts())
fig3 = px.bar(x=list(sub_status.keys()), y=list(sub_status.values()), title="Subscription status")"""

sub_status = dict(data.subscription_status.value_counts())
# fig3 = px.pie(values=list(sub_status.values()), names=list(sub_status.keys()),color_discrete_sequence= ["#003f5c", "#668eaa"], title="<b>Subscription status</b>",)
fig3 = go.Figure(
    data=[
        go.Pie(
            labels=list(sub_status.keys()),
            values=list(sub_status.values()),
            pull=[0, 0.1],
        )
    ]
)
fig3.update_layout(title_text="<b>Subscription status</b>")
fig3.update_traces(marker=dict(colors=["#2c3e50", "#e74c3c"]))

cust_class = dict(data.customer_class.value_counts())
fig4 = px.bar(
    x=list(cust_class.keys()),
    y=list(cust_class.values()),
    color=colour[:3],
    color_discrete_map="identity",
    title="<b>Customer class</b>",
    labels={"x": "Customer class", "y": "Number of users"},
)

churn = dict(data.churn.value_counts())
fig5 = px.bar(
    x=list(churn.keys()),
    y=list(churn.values()),
    color=colour[:2],
    color_discrete_map="identity",
    title="<b>Churn</b>",
    labels={"x": "Churn", "y": "Number of users"},
)

## roc curve plot


# def serve_roc_curve():

#     fpr, tpr, threshold = roc_curve(df_churn, preds)
#     auc_score = roc_auc_score(y_true=df_churn, y_score=preds)

#     trace0 = go.Scatter(
#         x=fpr, y=tpr, mode="lines", name="Test Data", marker={"color": "#13c6e9"}
#     )

#     # gridcolor = '#F8F8F8' # White
#     gridcolor = '#2f3445'

#     layout = go.Layout(
#         title=f"ROC Curve (AUC = {auc_score:.3f})",
#         xaxis=dict(title="False Positive Rate", gridcolor="#2f3445"),
#         yaxis=dict(title="True Positive Rate", gridcolor="#2f3445"),
#         legend=dict(x=0, y=1.05, orientation="h"),
#         margin=dict(l=100, r=10, t=25, b=40),
#         #plot_bgcolor="#282b38",
#         #paper_bgcolor="#282b38",
#         font={"color": "#a5b1cd"},
#     )

#     data0 = [trace0]
#     figure = go.Figure(data=data0, layout=layout)

#     return figure


# def serve_pie_confusion_matrix():
#     # Compute threshold
#     #     scaled_threshold = threshold * (Z.max() - Z.min()) + Z.min()
#     #     y_pred_test = (model.decision_function(X_test) > scaled_threshold).astype(int)

#     matrix = confusion_matrix(y_true=df_churn, y_pred=preds)
#     tn, fp, fn, tp = matrix.ravel()

#     values = [tp, fn, fp, tn]
#     label_text = ["True Positive", "False Negative", "False Positive", "True Negative"]
#     labels = ["TP", "FN", "FP", "TN"]
#     blue = cl.flipper()["seq"]["9"]["Blues"]
#     red = cl.flipper()["seq"]["9"]["Reds"]
#     colors = ["#2c3e50", "#7ccc63", "#bdc3c7", "#f39c12", "#e74c3c"]

#     trace0 = go.Pie(
#         labels=label_text,
#         values=values,
#         hoverinfo="label+value+percent",
#         textinfo="text+value",
#         text=labels,
#         sort=False,
#         marker=dict(colors=colors),
#         insidetextfont={"color": "white"},
#         rotation=90,
#     )

#     layout = go.Layout(
#         title="Confusion Matrix",
#         margin=dict(l=50, r=50, t=100, b=10),
#         legend=dict(bgcolor="#282b38", font={"color": "#a5b1cd"}, orientation="h"),
#         plot_bgcolor="#282b38",
#         paper_bgcolor="#282b38",
#         font={"color": "#a5b1cd"},
#     )

#     data0 = [trace0]
#     figure = go.Figure(data=data0, layout=layout)

#     return figure

pred_churn = dict(data_pred["pred_churn"].value_counts())
fig_pred_churn = px.bar(
    x=list(pred_churn.keys()),
    y=list(pred_churn.values()),
    color=colour[:2],
    color_discrete_map="identity",
    title="<b>Churn</b>",
    labels={"x": "Churn", "y": "Number of users"},
)
