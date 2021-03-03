import plotly.express as px
import plotly.graph_objects as go
from data_reader import data


colour = ["#2c3e50", "#e74c3c", "#bdc3c7", "#f39c12", "#7ccc63"]


ott_subs = dict(data.ott_subscription.value_counts())
fig = px.bar(x=list(ott_subs.keys()), y=list(ott_subs.values()), color=colour, color_discrete_map="identity", title="<b>Popularity of OTT Platform</b>",
             labels={'x': 'OTT Platforms', 'y': 'Number of users'}
             )

dth_pack = dict(data.dth_pack.value_counts())
'''fig2 = px.bar(x=list(dth_pack.keys()), y=list(dth_pack.values()), color=colour[:3], color_discrete_map="identity", title="<b>DTH Pack distribution</b>",
              labels={'x':'DTH Pack Type', 'y':'Number of users'}
              )'''

fig2 = go.Figure(
    data=[go.Pie(labels=list(dth_pack.keys()), values=list(dth_pack.values()))])
fig2.update_layout(title_text="<b> DTH Pack distribution </b>")
fig2.update_traces(marker=dict(colors=["#2c3e50", "#e74c3c", "#bdc3c7"]))

'''sub_status = dict(data.subscription_status.value_counts())
fig3 = px.bar(x=list(sub_status.keys()), y=list(sub_status.values()), title="Subscription status")'''

sub_status = dict(data.subscription_status.value_counts())
# fig3 = px.pie(values=list(sub_status.values()), names=list(sub_status.keys()),color_discrete_sequence= ["#003f5c", "#668eaa"], title="<b>Subscription status</b>",)
fig3 = go.Figure(data=[go.Pie(labels=list(sub_status.keys()),
                              values=list(sub_status.values()), pull=[0, 0.1])])
fig3.update_layout(title_text="<b>Subscription status</b>")
fig3.update_traces(marker=dict(colors=["#2c3e50", "#e74c3c"]))

cust_class = dict(data.customer_class.value_counts())
fig4 = px.bar(x=list(cust_class.keys()), y=list(cust_class.values()), color=colour[:3], color_discrete_map="identity", title="<b>Customer class</b>",
              labels={'x': 'Customer class', 'y': 'Number of users'}
              )

churn = dict(data.churn.value_counts())
fig5 = px.bar(x=list(churn.keys()), y=list(churn.values()), color=colour[:2], color_discrete_map="identity", title="<b>Churn</b>",
              labels={'x': 'Churn', 'y': 'Number of users'}
              )
