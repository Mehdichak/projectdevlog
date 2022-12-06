import pandas as pd
import numpy as np

class min_max:
    def __init__(self, id):
        self.id = id
    
    def max(self,x,u):
        y = x[x['Num_dept'] == self.id]
        a = y['Consommation (MWh)'].max()
        b = y[y['Consommation (MWh)'] == a]
        b = b['nom']
        print('La consommation max du département',self.id, "pour l'année", u ,'est de' ,a, 'dans la commune de', b)

    def min(self,x,u):
        y = x[x['Num_dept'] == self.id]
        a = y['Consommation (MWh)'].min()
        b = y[y['Consommation (MWh)'] == a]
        b = b['nom']
        print('La consommation min du département',self.id, "pour l'année", u , 'est de' ,a, 'dans la commune de', b)

def somme_conso(x):
    i=0
    m=[]
    for i in range(95):
        datatemp = x[ x['Num_dept'].apply(lambda x: int(str(x)[:-3])) == i+1 ]
        Total = datatemp['Consommation (MWh)'].sum()
        m = m + [Total]
        i = i+1
    return m

def dept_num():
    i = 0
    m = []
    for i in range(95):
        m = m + [i+1]
        i = i+1
    return m

def fct_min_max(x):

    #Chargement des données
    data_2018 = pd.read_csv("./predivis/data/Conso2018.csv", sep=';')
    data_2019 = pd.read_csv("./predivis/data/Conso2019.csv", sep=';')
    data_2020 = pd.read_csv("./predivis/data/Conso2020.csv", sep=';')
    data_2021 = pd.read_csv("./predivis/data/Conso2021.csv", sep=';')

    #Nettoyage des données
    data_2018.drop_duplicates(inplace=True)
    data_2018.dropna(inplace=True)
    data_2018 = data_2018.rename(columns={"Code INSEE de la commune": "Num_dept", "Nom de la commune": "nom",
                            "Consommation annuelle moyenne de la commune (MWh)": "Consommation (MWh)"})
    data_2019.drop_duplicates(inplace=True)
    data_2019.dropna(inplace=True)
    data_2019 = data_2019.rename(columns={"Code INSEE de la commune": "Num_dept", "Nom de la commune": "nom",
                            "Consommation annuelle moyenne de la commune (MWh)": "Consommation (MWh)"})
    data_2020.drop_duplicates(inplace=True)
    data_2020.dropna(inplace=True)
    data_2020 = data_2020.rename(columns={"Code INSEE de la commune": "Num_dept", "Nom de la commune": "nom",
                            "Consommation annuelle moyenne de la commune (MWh)": "Consommation (MWh)"})
    data_2021.drop_duplicates(inplace=True)
    data_2021.dropna(inplace=True)
    data_2021 = data_2021.rename(columns={"Code INSEE de la commune": "Num_dept", "Nom de la commune": "nom",
                            "Consommation annuelle moyenne de la commune (MWh)": "Consommation (MWh)"})

    #Transformation des codes insee en numéro de département
    data_2018["Num_dept"] = data_2018["Num_dept"].apply(lambda x: int(str(x)[:-3]))

    data_2019["Num_dept"] = data_2019["Num_dept"].apply(lambda x: int(str(x)[:-3]))

    data_2020["Num_dept"] = data_2020["Num_dept"].apply(lambda x: int(str(x)[:-3]))

    data_2021["Num_dept"] = data_2021["Num_dept"].apply(lambda x: int(str(x)[:-3]))

    i = 0
    year = 2018
    for i in range(4):
        if year == 2018:
            min_max(x).max(data_2018,year)
            min_max(x).min(data_2018,year)
        else:
            if year == 2019:
                min_max(x).max(data_2019,year)
                min_max(x).min(data_2019,year)
            else:
                if year == 2020:
                    min_max(x).max(data_2020,year)
                    min_max(x).min(data_2020,year)
                else:
                    min_max(x).max(data_2021,year)
                    min_max(x).min(data_2021,year)
        year = year + 1
        i = i + 1