import pandas as pd
import matplotlib as plt
import datetime
# On charge le fichier csv en tant que dataframe
filepath="predictiondata.csv"
table = pd.read_csv(filepath,sep=";")

# On enlève les données non utiles
table=table.drop(columns=["Périmètre","Nature","Ech. comm. Angleterre (MW)","Ech. comm. Espagne (MW)","Ech. comm. Italie (MW)","Ech. comm. Suisse (MW)","Ech. comm. Allemagne-Belgique (MW)","Stockage batterie (MW)","Déstockage batterie (MW)","Eolien terrestre (MW)","Eolien offshore (MW)"])

# On enlève les lignes qui ont des données manquantes
table = table.dropna()

# On selectionne comme index la donnée temporelle
table = table.set_index("Date - Heure")
print(table.head())
print(table.info())

plt
