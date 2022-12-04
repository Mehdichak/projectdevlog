import requests
import pandas as pd
import datetime
import os

# On télécharge les données énedis dans deux fichiers 
print("Télechargement des données de long-terme")
URL1 = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/download/?format=csv&disjunctive.nature=true&q=date_heure%3E%3D%222020-05-30T22:00:00Z%22&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
r = requests.get(URL1)
print(r)
open("LongTermData.csv","wb").write(r.content)
print("Données de long terme téléchargées")

print("Télechargement des données de court-terme")
URL2 = "https://odre.opendatasoft.com/explore/dataset/eco2mix-national-tr/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
r = requests.get(URL2)
print(r)
open("ShortTermData.csv","wb").write(r.content)
print("Données de court-terme téléchargées")

# On charge les fichier csv en tant que dataframes
filepath="ShortTermData.csv"
filepath2="LongTermData.csv"
table = pd.read_csv(filepath,sep=";")
table2 = pd.read_csv(filepath2,sep=";")

# On enlève les données non utiles, on fait en sorte d'avoir les memes colonnes sur les deux tables
table=table.drop(columns=["Prévision J (MW)","Prévision J-1 (MW)","Périmètre","Nature","Ech. comm. Angleterre (MW)","Ech. comm. Espagne (MW)","Ech. comm. Italie (MW)","Ech. comm. Suisse (MW)","Ech. comm. Allemagne-Belgique (MW)","Stockage batterie (MW)","Déstockage batterie (MW)","Eolien terrestre (MW)","Eolien offshore (MW)"])
table2=table2.drop(columns=["Prévision J (MW)","Périmètre","Prévision J-1 (MW)","Nature","Ech. comm. Angleterre (MW)","Ech. comm. Espagne (MW)","Ech. comm. Italie (MW)","Ech. comm. Suisse (MW)","Ech. comm. Allemagne-Belgique (MW)"])
table = table.dropna()

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

# On interpole des données linéairement pour obtenir un index temporel de meme fréquence que la prédiction souhaitée
table2 = table2.interpolate(method="linear")

# On fusionne les données des deux tables sources
table2  = table2.append(table)
table2 = table2.sort_index(ascending=True)

# On construit un csv
table2.to_csv(sep=";",path_or_buf="PredictionCleanData.csv")
print("Données nettoyées et intégrées dans le fichier PredictionCleanData.csv")

#On supprime les fichiers créés au début de la manipulation
os.remove(LongTermData.csv)
os.remove(ShortTermData.csv)

