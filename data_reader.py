import pandas as pd
from joblib import dump, load
import warnings


warnings.filterwarnings("ignore")

## read data
data = pd.read_csv("./data/dth_data_1.csv")  ## train data
data_pred = pd.read_csv("./data/df_train_all_pred.csv")  ## predictions on all training data
test_data = pd.read_csv("./data/dth_test_data_5k.csv")  ## test data
pred_changes = pd.read_csv("./data/df_final_pred_change.csv")  ## csv showing only changes in churn

## read models
xgboost_model = load("./saved_models/xgb01.dat")

# Query to fetch data in dashboard
active_customer = dict(data.subscription_status.value_counts())
active_customer = active_customer[True]

total_customer = len(data)

churn_rate = dict(data.churn.value_counts())
churn_rate = (churn_rate[True] / (churn_rate[False] + churn_rate[True])) * 100

expected_monthly_income = data[data["subscription_status"] == True]["dth_pack_price"].sum()


pred_churn_list = data_pred["pred_churn"].value_counts().to_list()
pred_churn_list_true = data_pred["pred_churn"].value_counts().to_list()[1]
pred_churn_count_percent = pred_churn_list[1] / (pred_churn_list[0] + pred_churn_list[1])


def get_df_churn(df):
    df_cols = df.columns.to_list()
    df_churn = []

    if "churn" in df_cols:
        df_churn = df[["churn"]]

    return df_churn


def get_predictions(df):

    df_cols = df.columns.to_list()
    df_cust_details = df[["names", "address", "city", "phone_number"]]

    # df_cust_details

    df_churn = []

    if "churn" in df_cols:
        df_churn = df[["churn"]]

    cust_details_cols = df_cust_details.columns.to_list()

    df.drop(columns=cust_details_cols, axis=1, inplace=True)
    # df
    if "churn" in df_cols:
        df.drop(columns=["churn"], axis=1, inplace=True)
    # df
    df["subscription_status"] = df["subscription_status"].astype("category")
    df["subscription_status"] = df["subscription_status"].cat.codes
    df["subscription_status"] = df["subscription_status"].astype("int64")

    df = pd.get_dummies(df)
    df

    xgb_test = load("./saved_models/xgb01.dat")

    cols_when_model_build = xgb_test.get_booster().feature_names
    df = df[cols_when_model_build]

    preds = xgb_test.predict(df)

    return preds



data_copy = data.copy()
df_churn = get_df_churn(data_copy)
preds = get_predictions(data_copy)

