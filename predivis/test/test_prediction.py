import predivis
import pandas as pd

def test_dataload():
    assert predivis.prediction.dataloading() == 1
def test_Methode_Prophet():
    assert isinstance(predivis.prediction.predict_for_day(filepath="PredictionCleanData.csv",filepath_out="prediction.csv", date_initiale='2022-11-15', methode='Prophet', source_conso="Consommation (MW)", date_prediction='2022-12-08', save_model=False, load_model=False) , pd.DataFrame)
def test_methodeHoltWinters():
    assert isinstance(predivis.prediction.predict_for_day(methode="Holt_Winters",date_initiale='2022-11-15'), pd.DataFrame)

