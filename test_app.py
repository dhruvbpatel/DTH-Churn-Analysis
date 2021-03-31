from data_reader import *
from layouts import serve_roc_curve,serve_pie_confusion_matrix,no_with_comma,no_to_percentage
import pytest

## test to check if data is imported properly
def test_data_import():
    assert data.empty == False
    assert data_pred.empty == False
    assert test_data.empty == False
    assert pred_changes.empty == False
    assert pred_sentiment.empty == False

## to check the values in home page container box
def test_container_data():
    assert total_customer is not None
    assert active_customer is not None
    assert churn_rate is not None
    assert expected_monthly_income is not None

# to check the values in churn data tab container box
def test_churn_data_container_data():
    assert pred_churn_count_percent is not None
    assert pred_churn_list_true is not None

## check comma and percentage convertion function
@pytest.mark.parametrize("test_val,expected_res",[
    (10,"10"),
    (100,"100"),
    (1000,"1,000"),
    (10000,"10,000"),
    (100000,"100,000"),
    (1000000,"1,000,000"),
    (10.22, "10.22"),
    (1000.22, "1,000.22")

])
def test_comma_func(test_val,expected_res):  
    assert no_with_comma(test_val) == expected_res

## check percentage convertion function
@pytest.mark.parametrize("test_val,expected_res", [
    (10, "10.00%"),
    (1000, "1000.00%"),
    (000100.22,"100.22%"),
    (100.99999,"101.00%"),
    (100.988,"100.99%")
])
def test_percent_func(test_val, expected_res):
    assert no_to_percentage(test_val) == expected_res
