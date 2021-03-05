import pandas as pd

data = pd.read_csv("dth_data_1.csv")
data_pred = pd.read_csv("./saved_models/train_data_X_pred_xgb01_70acc.csv")


# Query to fetch data in dashboard
active_customer = dict(data.subscription_status.value_counts())
active_customer = active_customer[True]

total_customer = len(data)

churn_rate = dict(data.churn.value_counts())
churn_rate = (churn_rate[True]/(churn_rate[False]+churn_rate[True]))*100

expected_monthly_income = data[data["subscription_status"]
                               == True]["dth_pack_price"].sum()

