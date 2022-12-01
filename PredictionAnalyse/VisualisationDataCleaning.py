import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

# On charge le fichier csv en tant que dataframe
filepath="VisualisationData.csv"
table = pd.read_csv(filepath,sep=";")
print(table.info())
table = table.drop(columns=["Code IRIS","Nom IRIS","Numéro de voie","Indice de répétition","Type de voie","Libellé de voie","Segment de client","Nombre de logements","Adresse","Tri des adresses","Nom de la commune"])
table = table.set_index("Code INSEE de la commune")
table2=table.groupby(["Code INSEE de la commune","Année"]).mean()
print(table2.info())
table.to_csv(path_or_buf="VisualisationCleanData",sep=";")
table2 = table2.dropna()
table2.to_csv(path_or_buf="VisualisationMeanCleanData",sep=";")