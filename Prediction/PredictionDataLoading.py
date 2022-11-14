import pandas as pd
filepath="predictiondata.csv"
table = pd.read_csv(filepath,sep=";")
table.info()
table=table.drop(columns=["Périmètre","Nature","Date","Heure","Ech. comm. Angleterre (MW)","Ech. comm. Espagne (MW)","Ech. comm. Italie (MW)","Ech. comm. Suisse (MW)","Ech. comm. Allemagne-Belgique (MW)","Stockage batterie (MW)","Déstockage batterie (MW)","Eolien terrestre (MW)","Eolien offshore (MW)"])
table.info()
table = table.dropna()
table.info()
print(table.head())