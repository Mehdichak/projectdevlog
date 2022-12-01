import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

table = pd.read_csv("PredictionCleanData.csv", sep=";")
longterm = pd.read_csv("LongTermCleanData.csv", sep=";")
table["Date - Heure"] = pd.to_datetime(table["Date - Heure"])
longterm["Date et Heure"] = pd.to_datetime(longterm["Date et Heure"])
table = table.set_index("Date - Heure")
longterm = longterm.set_index("Date et Heure")



table2 = table - table.shift(7,freq="D")
table2 = table2.dropna()
table3 = table - table.shift(1,freq="D")
table3 = table3.dropna()

table2.to_csv(sep=";",path_or_buf="WeekAgoComparaison.csv")
table3.to_csv(sep=";",path_or_buf="DayAgoComparaison.csv")

print((table2["Consommation (MW)"]*table2["Consommation (MW)"]).mean())
print((table3["Consommation (MW)"]*table3["Consommation (MW)"]).mean())

table["day"] = table.index.dayofyear
plt.plot(table["Consommation (MW)"].groupby(table.index.dayofyear).mean())
plt.show()

plt.plot(table["Consommation (MW)"])
plt.show()
plt.plot(longterm["Consommation (MW)"])
plt.show()
plt.plot(longterm["Consommation (MW)"].groupby(longterm.index.dayofyear).mean())
plt.show()