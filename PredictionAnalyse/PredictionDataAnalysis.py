import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

longterm = pd.read_csv("LongTermCleanData.csv", sep=";")
longterm["Date - Heure"] = pd.to_datetime(longterm["Date - Heure"])
longterm = longterm.set_index("Date - Heure")

# On regarde l'erreur des prédictions naives et naives saisonieres
NlongtermError = longterm - longterm.shift(15,freq="T")
NlongtermError = NlongtermError.dropna()
SNlongtermError = longterm - longterm.shift(365,freq="D")
SNlongtermError = SNlongtermError.dropna()

decomposition = seasonal_decompose(longterm["Consommation (MW)"], model='multiplicative', period=365*24*4)  
fig = decomposition.plot()
fig.set_size_inches(14, 7)
plt.show()


print((NlongtermError["Consommation (MW)"]*NlongtermError["Consommation (MW)"]).mean())
print((SNlongtermError["Consommation (MW)"]*SNlongtermError["Consommation (MW)"]).mean())
