import pandas as pd
import matplotlib.pyplot as plt
import datetime
from statsmodels.tsa.seasonal import seasonal_decompose

longterm = pd.read_csv("PredictionCleanData.csv", sep=";")
longterm["Date - Heure"] = pd.to_datetime(longterm["Date - Heure"])
longterm = longterm.set_index("Date - Heure")

# On regarde le décalage des prédictions naives et naives-saisonieres
NlongtermError = longterm - longterm.shift(15,freq="T")
NlongtermError = NlongtermError.dropna()
SNlongtermError = longterm - longterm.shift(365,freq="D")
SNlongtermError = SNlongtermError.dropna()

#Et on calcule l'erreur quadratique moyennes associées
print((NlongtermError["Consommation (MW)"]*NlongtermError["Consommation (MW)"]).mean())
print((SNlongtermError["Consommation (MW)"]*SNlongtermError["Consommation (MW)"]).mean())

# On regarde une décomposition saisonière multiplicative de notre série temporelle principale
decomposition = seasonal_decompose(longterm["Consommation (MW)"], model='multiplicative', period=365*24*4)  
fig = decomposition.plot()
fig.set_size_inches(14, 7)
plt.show()

# On regarde une décomposition seasonière additive de notre série temporelle principale
decomposition = seasonal_decompose(longterm["Consommation (MW)"], model='additive', period=365*24*4)  
fig = decomposition.plot()
fig.set_size_inches(14, 7)
plt.show()
