from data_reader import *

def test_data_import():
    assert data.empty == False
    assert data_pred.empty == False