import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose


longterm = pd.read_csv("LongTermCleanData.csv", sep=";")
longterm["Date - Heure"] = pd.to_datetime(longterm["Date - Heure"])
longterm = longterm.set_index("Date - Heure")

# On regarde l'erreur des prédictions naives et naives saisonieres
NlongtermError = longterm - longterm.shift(-900,freq="s")
NlongtermError = NlongtermError.dropna()
SNlongtermError = longterm - longterm.shift(-1,freq="y")
SNlongtermError = SNlongtermError.dropna()

print(seasonal_decompose(longterm[longterm.index<pd.to_datetime("2022-09-02")],period=7).info())

print((NlongtermError["Consommation (MW)"]*NlongtermError["Consommation (MW)"]).mean())
print((SNlongtermError["Consommation (MW)"]*SNlongtermError["Consommation (MW)"]).mean())


plt.plot(longterm["Consommation (MW)"].groupby(longterm.index.dayofyear).mean())
plt.show()

plt.plot(longterm["Consommation (MW)"])
plt.show()
