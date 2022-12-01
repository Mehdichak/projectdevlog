import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

# On charge le fichier csv en tant que dataframe
filepath="predictiondata.csv"
filepath2="LongTermData.csv"
table = pd.read_csv(filepath,sep=";")
table2 = pd.read_csv(filepath2,sep=";")
print(table2.info())


# On enlève les données non utiles
table=table.drop(columns=["Périmètre","Nature","Ech. comm. Angleterre (MW)","Ech. comm. Espagne (MW)","Ech. comm. Italie (MW)","Ech. comm. Suisse (MW)","Ech. comm. Allemagne-Belgique (MW)","Stockage batterie (MW)","Déstockage batterie (MW)","Eolien terrestre (MW)","Eolien offshore (MW)"])
table2=table2.drop(columns=["Périmètre","Prévision J-1 (MW)","Nature","Ech. comm. Angleterre (MW)","Ech. comm. Espagne (MW)","Ech. comm. Italie (MW)","Ech. comm. Suisse (MW)","Ech. comm. Allemagne-Belgique (MW)"])
table = table.dropna()
table2 = table2.dropna()


# On construit un index temporel adapté
table["Date - Heure"] = pd.to_datetime(table["Date"] + ' ' +table["Heure"])
table2["Date et Heure"] = pd.to_datetime(table2["Date"] + ' ' +table2["Heure"])
table2["Date - Heure"] = table2["Date et Heure"]
table=table.drop(columns=["Date","Heure"])
table2=table2.drop(columns=["Date","Heure"])
table2 = table2.drop(columns=["Date et Heure"])
table=table.set_index("Date - Heure")
table = table.sort_index(ascending=True)
table2=table2.set_index("Date - Heure")
table2 = table2.sort_index(ascending=True)


print(table.info())
print(table2.info())
# On construit un csv
table.to_csv(sep=";",path_or_buf="PredictionCleanData.csv")
table2.to_csv(sep=";",path_or_buf="LongTermCleanData.csv")
