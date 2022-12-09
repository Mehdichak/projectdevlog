import statsmodels.tsa.seasonal
import pandas as pd
import matplotlib.pyplot as plt
r = pd.read_csv("PredictionCleanData.csv",sep=";")
r["Date - Heure"] = pd.to_datetime(r["Date - Heure"])

r.set_index(["Date - Heure"],inplace=True)
r = r["Consommation (MW)"]
print(r)
statsmodels.tsa.seasonal.seasonal_decompose(r,period=24*4*365,extrapolate_trend=True,model="multiplicative").plot()
plt.show()
