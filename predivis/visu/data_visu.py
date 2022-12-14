import pandas as pd
import json
import numpy as np
import plotly.express as px
import plotly.io as pio

def sommeconso(x):
    """ Fonction qui va sommer la consommation moyenne des différentes communes pour tous les départements et les renvoyer en tant que liste. 

        Input :
            - x : Un dataframe contenant une colonne "Departement" et "Consommation (MWh)"
            
        Output :
            - m : Une liste des consommations (MWh) triée par ordre numérique des départements
    """
    i=0
    m=[]
    for i in range(95):
        datatemp = x[ x["Departement"] == i+1 ]
        Total = datatemp['Consommation (MWh)'].sum()
        m = m + [Total]
        i = i+1
    return m

def deptnum():
    """ Fonction qui va lister les nombres de 1 à 95 inclus.

        Output :
            - m : Une liste des nombres de 1 à 95 inclus.

    """
    i = 0
    m = []
    for i in range(95):
        m = m + [i+1]
        i = i+1
    return m


def Visumultiple():
    """ Fonction qui va créer 4 cartes de la consommation (MWh) pour chaque année selon un découpage départemental.

        Outputs :
            - Produit 4 cartes dans des onglets du navigateur internet par défaut.

    """
    pio.renderers.default = 'browser'

    #Chargement des données
    data_2018 = pd.read_csv("./predivis/data/Conso2018.csv", sep=';')
    data_2019 = pd.read_csv("./predivis/data/Conso2019.csv", sep=';')
    data_2020 = pd.read_csv("./predivis/data/Conso2020.csv", sep=';')
    data_2021 = pd.read_csv("./predivis/data/Conso2021.csv", sep=';')

    #Nettoyage des données
    data_2018.drop_duplicates(inplace=True)
    data_2018.dropna(inplace=True)
    data_2018 = data_2018.rename(columns={"Code INSEE de la commune": "Departement", "Nom de la commune": "nom",
                            "Consommation annuelle moyenne de la commune (MWh)": "Consommation (MWh)"})
    data_2019.drop_duplicates(inplace=True)
    data_2019.dropna(inplace=True)
    data_2019 = data_2019.rename(columns={"Code INSEE de la commune": "Departement", "Nom de la commune": "nom",
                            "Consommation annuelle moyenne de la commune (MWh)": "Consommation (MWh)"})
    data_2020.drop_duplicates(inplace=True)
    data_2020.dropna(inplace=True)
    data_2020 = data_2020.rename(columns={"Code INSEE de la commune": "Departement", "Nom de la commune": "nom",
                            "Consommation annuelle moyenne de la commune (MWh)": "Consommation (MWh)"})
    data_2021.drop_duplicates(inplace=True)
    data_2021.dropna(inplace=True)
    data_2021 = data_2021.rename(columns={"Code INSEE de la commune": "Departement", "Nom de la commune": "nom",
                            "Consommation annuelle moyenne de la commune (MWh)": "Consommation (MWh)"})


    #Transformation des codes insee en numéro de département
    data_2018['Departement'] = data_2018['Departement'].apply(lambda x: int(str(x)[:-3]))

    data_2019['Departement'] = data_2019['Departement'].apply(lambda x: int(str(x)[:-3]))

    data_2020['Departement'] = data_2020['Departement'].apply(lambda x: int(str(x)[:-3]))

    data_2021['Departement'] = data_2021['Departement'].apply(lambda x: int(str(x)[:-3]))

    #Data des sommes de consommation par département
    data_final = {'Numero':deptnum(),'Nom_dept':['Ain','Aisne','Allier','Alpes de Haute-Provence','Hautes-Alpes','Alpes-Maritimes','Ardêche','Ardennes','Ariège','Aube','Aude','Aveyron','Bouches-du-Rhône','Calvados','Cantal','Charente','Charente-Maritime','Cher','Corrèze','Corse',"Côte-d'Or","Côtes d'Armor",'Creuse','Dordogne','Doubs','Drôme','Eure','Eure-et-Loire','Finistère','Gard','Haute-Garonne','Gers','Gironde','Hérault','île-et-vilaine','Indre','Indre-et-Loire','Isère','Jura','Landres','Loir-et-Cher','Loire','Haute-Loire','Loire-Atlantique','Loiret','Lot','Lot-et-Garonne','Lozère','Maine-et-Loire','Manche','Marne','Haute-Marne','Mayenne','Meurthe-et-Moselle','Meuse','Morbihan','Moselle','Nièvre','Nord','Oise','Orne','Pas-de-Calais','Puy-de-Dôme','Pyrénées-Atlantique','Hautes-Pyrénées','Pyrénées-Orientales','Bas-Rhin','Haut-Rhin','Rhône','Haute-Saône','Saône-et-Loire','Sarthe','Savoie','Haute-Savoie','Paris','Seine-Maritime','Seine-et-Marne','Yvelines','Deux-Sèvres','Somme','Tarn','Tarn-et-Garonne','Var','Vaucluse','Vendée','Vienne','Haute-Vienne','Vosges','Yonne','Territoire-de-Belfort','Essone','Hauts-de-Seine','Seine-Saint-Denis','Val-de-Marne',"Val-d'Oise"], 'Consommation (MWh)':sommeconso(data_2018)}
    df_2018 = pd.DataFrame(data_final)

    data_final = {'Numero':deptnum(),'Nom_dept':['Ain','Aisne','Allier','Alpes de Haute-Provence','Hautes-Alpes','Alpes-Maritimes','Ardêche','Ardennes','Ariège','Aube','Aude','Aveyron','Bouches-du-Rhône','Calvados','Cantal','Charente','Charente-Maritime','Cher','Corrèze','Corse',"Côte-d'Or","Côtes d'Armor",'Creuse','Dordogne','Doubs','Drôme','Eure','Eure-et-Loire','Finistère','Gard','Haute-Garonne','Gers','Gironde','Hérault','île-et-vilaine','Indre','Indre-et-Loire','Isère','Jura','Landres','Loir-et-Cher','Loire','Haute-Loire','Loire-Atlantique','Loiret','Lot','Lot-et-Garonne','Lozère','Maine-et-Loire','Manche','Marne','Haute-Marne','Mayenne','Meurthe-et-Moselle','Meuse','Morbihan','Moselle','Nièvre','Nord','Oise','Orne','Pas-de-Calais','Puy-de-Dôme','Pyrénées-Atlantique','Hautes-Pyrénées','Pyrénées-Orientales','Bas-Rhin','Haut-Rhin','Rhône','Haute-Saône','Saône-et-Loire','Sarthe','Savoie','Haute-Savoie','Paris','Seine-Maritime','Seine-et-Marne','Yvelines','Deux-Sèvres','Somme','Tarn','Tarn-et-Garonne','Var','Vaucluse','Vendée','Vienne','Haute-Vienne','Vosges','Yonne','Territoire-de-Belfort','Essone','Hauts-de-Seine','Seine-Saint-Denis','Val-de-Marne',"Val-d'Oise"], 'Consommation (MWh)':sommeconso(data_2019)}
    df_2019 = pd.DataFrame(data_final)

    data_final = {'Numero':deptnum(),'Nom_dept':['Ain','Aisne','Allier','Alpes de Haute-Provence','Hautes-Alpes','Alpes-Maritimes','Ardêche','Ardennes','Ariège','Aube','Aude','Aveyron','Bouches-du-Rhône','Calvados','Cantal','Charente','Charente-Maritime','Cher','Corrèze','Corse',"Côte-d'Or","Côtes d'Armor",'Creuse','Dordogne','Doubs','Drôme','Eure','Eure-et-Loire','Finistère','Gard','Haute-Garonne','Gers','Gironde','Hérault','île-et-vilaine','Indre','Indre-et-Loire','Isère','Jura','Landres','Loir-et-Cher','Loire','Haute-Loire','Loire-Atlantique','Loiret','Lot','Lot-et-Garonne','Lozère','Maine-et-Loire','Manche','Marne','Haute-Marne','Mayenne','Meurthe-et-Moselle','Meuse','Morbihan','Moselle','Nièvre','Nord','Oise','Orne','Pas-de-Calais','Puy-de-Dôme','Pyrénées-Atlantique','Hautes-Pyrénées','Pyrénées-Orientales','Bas-Rhin','Haut-Rhin','Rhône','Haute-Saône','Saône-et-Loire','Sarthe','Savoie','Haute-Savoie','Paris','Seine-Maritime','Seine-et-Marne','Yvelines','Deux-Sèvres','Somme','Tarn','Tarn-et-Garonne','Var','Vaucluse','Vendée','Vienne','Haute-Vienne','Vosges','Yonne','Territoire-de-Belfort','Essone','Hauts-de-Seine','Seine-Saint-Denis','Val-de-Marne',"Val-d'Oise"], 'Consommation (MWh)':sommeconso(data_2020)}
    df_2020 = pd.DataFrame(data_final)

    data_final = {'Numero':deptnum(),'Nom_dept':['Ain','Aisne','Allier','Alpes de Haute-Provence','Hautes-Alpes','Alpes-Maritimes','Ardêche','Ardennes','Ariège','Aube','Aude','Aveyron','Bouches-du-Rhône','Calvados','Cantal','Charente','Charente-Maritime','Cher','Corrèze','Corse',"Côte-d'Or","Côtes d'Armor",'Creuse','Dordogne','Doubs','Drôme','Eure','Eure-et-Loire','Finistère','Gard','Haute-Garonne','Gers','Gironde','Hérault','île-et-vilaine','Indre','Indre-et-Loire','Isère','Jura','Landres','Loir-et-Cher','Loire','Haute-Loire','Loire-Atlantique','Loiret','Lot','Lot-et-Garonne','Lozère','Maine-et-Loire','Manche','Marne','Haute-Marne','Mayenne','Meurthe-et-Moselle','Meuse','Morbihan','Moselle','Nièvre','Nord','Oise','Orne','Pas-de-Calais','Puy-de-Dôme','Pyrénées-Atlantique','Hautes-Pyrénées','Pyrénées-Orientales','Bas-Rhin','Haut-Rhin','Rhône','Haute-Saône','Saône-et-Loire','Sarthe','Savoie','Haute-Savoie','Paris','Seine-Maritime','Seine-et-Marne','Yvelines','Deux-Sèvres','Somme','Tarn','Tarn-et-Garonne','Var','Vaucluse','Vendée','Vienne','Haute-Vienne','Vosges','Yonne','Territoire-de-Belfort','Essone','Hauts-de-Seine','Seine-Saint-Denis','Val-de-Marne',"Val-d'Oise"], 'Consommation (MWh)':sommeconso(data_2021)}
    df_2021 = pd.DataFrame(data_final)



    #Création de la Carte de France
    Map = json.load(open("./predivis/data/departements.geojson", "r"))
    state_id_map = {}
    for feature in Map["features"]:
        feature["id"] = feature["properties"]["code"]
        state_id_map[feature["properties"]["nom"]] = feature["id"]

    #Figure de la consommation en 2018
    fig_2018 = px.choropleth_mapbox(
        df_2018,
        locations="Numero",
        geojson=Map,
        color="Consommation (MWh)",
        hover_name="Nom_dept",
        hover_data=["Consommation (MWh)"],
        title="Average electricity consumption(MWh) in France by departments in 2018",
        mapbox_style="carto-positron",
        center={"lat": 47, "lon": 2},
        zoom=4,
        opacity=0.5,
    )
    fig_2018.show()

    #Figure de la consommation en 2019
    fig_2019 = px.choropleth_mapbox(
        df_2019,
        locations="Numero",
        geojson=Map,
        color="Consommation (MWh)",
        hover_name="Nom_dept",
        hover_data=["Consommation (MWh)"],
        title="Average electricity consumption(MWh) in France by departments in 2019",
        mapbox_style="carto-positron",
        center={"lat": 47, "lon": 2},
        zoom=4,
        opacity=0.5,
    )
    fig_2019.show()

    #Figure de la consommation en 2020
    fig_2020 = px.choropleth_mapbox(
        df_2020,
        locations="Numero",
        geojson=Map,
        color="Consommation (MWh)",
        hover_name="Nom_dept",
        hover_data=["Consommation (MWh)"],
        title="Average electricity consumption(MWh) in France by departments in 2020",
        mapbox_style="carto-positron",
        center={"lat": 47, "lon": 2},
        zoom=4,
        opacity=0.5,
    )
    fig_2020.show()

    #Figure de la consommation en 2021
    fig_2021 = px.choropleth_mapbox(
        df_2021,
        locations="Numero",
        geojson=Map,
        color="Consommation (MWh)",
        hover_name="Nom_dept",
        hover_data=["Consommation (MWh)"],
        title="Average electricity consumption(MWh) in France by departments in 2021",
        mapbox_style="carto-positron",
        center={"lat": 47, "lon": 2},
        zoom=4,
        opacity=0.5,
    )
    fig_2021.show()
    return 1