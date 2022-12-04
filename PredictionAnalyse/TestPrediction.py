import pandas as pd
import datetime
from statsmodels.tsa.holtwinters import ExponentialSmoothing, SimpleExpSmoothing, Holt
import matplotlib.pyplot  as plt

Data = pd.read_csv("LongTermCleanData.csv", sep=";")
Data["Date - Heure"] = pd.to_datetime(Data["Date - Heure"])
Data = Data.set_index("Date - Heure")


DataToFit = Data["Consommation (MW)"]['2020-01-01':'2022-01-01'].resample("30T").mean()
DataToPredict = Data["Consommation (MW)"]['2022-01-01':'2022-01-27']



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
DataToPredict.plot(style='--', color='green', label='test')
plt.show()