import predivis

#predivis.prediction.dataloading(finalfilepath="PredictionCleanData.csv")
#predivis.prediction.predict_for_day(filepath="PredictionCleanData.csv",filepath_out="prediction.csv", date_initiale='2021-12-07', methode='Prophet', source_conso="Consommation (MW)", date_prediction='2022-12-08', save_model=False, load_model=False)
predivis.prediction.predict_for_day(methode="Holt_Winters",date_initiale='2022-11-15')

#predivis.visu.visu_final()
#predivis.visu.visu_unique()
#predivis.visu.visu_multiple()



