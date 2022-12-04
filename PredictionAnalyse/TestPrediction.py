import pandas as pd
import datetime
from statsmodels.tsa.holtwinters import ExponentialSmoothing, SimpleExpSmoothing, Holt
import matplotlib.pyplot  as plt

Data = pd.read_csv("PredictionCleanData.csv", sep=";")
Data["Date - Heure"] = pd.to_datetime(Data["Date - Heure"])
Data = Data.set_index("Date - Heure")


DataToFit = Data["Consommation (MW)"]['2020-05-31':'2022-05-31'].resample("30T").mean()
DataToPredict = Data["Consommation (MW)"]['2022-06-01':'2022-06-03']



Fit = ExponentialSmoothing(
    DataToFit,
    seasonal_periods=2*24*365,
    trend="add",
    seasonal="add",
    use_boxcox=True,
    freq = "30T",
    initialization_method="estimated"
).fit()

Fit.fittedvalues.plot(style='--', color='red', label='train')
plt.show()

DataToPredict.plot(style='--', color='blue', label='test')
Fit.Forecast(2*24*2).plot(style='--', color='yellow', label='prediction')
plt.show()