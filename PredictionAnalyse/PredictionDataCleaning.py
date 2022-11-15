import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

# On charge le fichier csv en tant que dataframe
filepath="predictiondata.csv"
table = pd.read_csv(filepath,sep=";")

# On enlève les données non utiles
table=table.drop(columns=["Périmètre","Nature","Ech. comm. Angleterre (MW)","Ech. comm. Espagne (MW)","Ech. comm. Italie (MW)","Ech. comm. Suisse (MW)","Ech. comm. Allemagne-Belgique (MW)","Stockage batterie (MW)","Déstockage batterie (MW)","Eolien terrestre (MW)","Eolien offshore (MW)"])

# On enlève les lignes qui ont des données manquantes
table = table.dropna()

# On selectionne comme index la donnée temporelle
table = table.set_index("Date - Heure")
table.to_csv(sep=";",path_or_buf="PredictionCleanData.csv")
print(table.head())
print(table.info())

# On crée les moyennes horaires et journalière de chaque valeur pour chaque heure et chaque jour 
HourMean = table.groupby(['Heure']).mean()
DateMean = table.groupby(['Date']).mean()

HourVar = table.groupby(['Heure']).var()
DateVar = table.groupby(['Date']).var()


fig, ax = plt.subplots()
ax.plot(DateMean["Consommation (MW)"])
plt.show()
