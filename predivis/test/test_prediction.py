import predivis
import pandas as pd

def test_predict_for_day():
    assert isinstance(predivis.prediction.predict_for_day() , pd.DataFrame)
def test_dataload():
    assert predivis.prediction.dataloading() == 1