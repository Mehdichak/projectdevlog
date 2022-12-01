import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

table = pd.read_csv("PredictionCleanData.csv", sep=";")
table["Date - Heure"] = pd.to_datetime(table["Date - Heure"])
table = table.set_index("Date - Heure")



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
Daymean = table * 0
for i in range(365) :
    Daymean = Daymean +  table[table["day"] == i] * table.groupby(table.index.dayofyear).mean()

table4 = table - Daymean

plt.plot(table["Consommation (MW)"])
plt.show()