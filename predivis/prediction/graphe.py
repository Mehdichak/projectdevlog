import pandas as pd
import matplotlib.pyplot as plt

actual = pd.read_csv("actual.csv",sep=";")
table = pd.read_csv("prediction2.csv",sep=",")
table2 = pd.read_csv("prediction3.csv",sep=",")
print(table)
actual["Date - Heure"] = pd.to_datetime(actual["Date"] + " " + actual["Heure"])
actual.set_index(["Date - Heure"],inplace=True)
actual.sort_index(inplace=True)
print(table2)
table2["Date - Heure"] = table["ds"]
print(table2)
table["Date - Heure"]=pd.to_datetime(table["ds"])
table2["Date - Heure"] = pd.to_datetime(table2["Date - Heure"])
table2.set_index(["Date - Heure"],inplace=True)
table.set_index(["Date - Heure"],inplace=True)
table2=table2["Additive"]["2022-12-07 00:00":"2022-12-07 23:59"]
table=table["yhat"]["2022-12-07 00:00":"2022-12-07 23:59"]
actual = actual["Consommation (MW)"]["2022-12-07 00:00":"2022-12-07 23:59"]
actual=actual
print(actual)
table2.plot(ylabel="Consommation (MW)")
table.plot()
actual.plot()

plt.show()
