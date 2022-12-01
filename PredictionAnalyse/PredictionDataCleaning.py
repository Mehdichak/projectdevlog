import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

# On charge le fichier csv en tant que dataframe
filepath="predictiondata.csv"
table = pd.read_csv(filepath,sep=";")

# On enlève les données non utiles
table=table.drop(columns=["Périmètre","Nature","Ech. comm. Angleterre (MW)","Ech. comm. Espagne (MW)","Ech. comm. Italie (MW)","Ech. comm. Suisse (MW)","Ech. comm. Allemagne-Belgique (MW)","Stockage batterie (MW)","Déstockage batterie (MW)","Eolien terrestre (MW)","Eolien offshore (MW)"])
table = table.dropna()


# On construit un index temporel adapté
table["Date - Heure"] = pd.to_datetime(table["Date"] + ' ' +table["Heure"])
table=table.drop(columns=["Date","Heure"])
table=table.set_index("Date - Heure")
table = table.sort_index(ascending=True)


print(table.info())

# On construit un csv
table.to_csv(sep=";",path_or_buf="PredictionCleanData.csv")
