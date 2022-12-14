import pandas as pd
import json
import numpy as np
import plotly.express as px
import plotly.io as pio
from dash import Dash, dcc, html, Input, Output

pio.renderers.default = 'browser'

def somme_conso(x):
    """ Fonction qui va sommer la consommation moyenne des différentes communes pour tous les départements et les renvoyer en tant que liste.

        Input :
            - x : Un dataframe contenant une colonne "Departement" et "Consommation (MWh)"
        
        Output :
            - m : Une liste des consommations (MWh) triée par ordre numérique des départements
    """
    i=0
    m=[]
    for i in range(95):
        datatemp = x[ x['Num_dept'].apply(lambda x: int(str(x)[:-3])) == i+1 ]
        Total = datatemp['Consommation (MWh)'].sum()
        m = m + [Total]
        i = i+1
    return m

def dept_num():
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

def Visu_Final():
    """ Fonction qui va créer un lien local afin de consulter la visualisation sur un navigateur internet.

        Create : 
            - Lien local vers la visualisation 
            
    """
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

    #Data des sommes de consommation par département
    data_final = {'Num_dept':dept_num(),'Nom_dept':['Ain','Aisne','Allier','Alpes de Haute-Provence','Hautes-Alpes','Alpes-Maritimes','Ardêche','Ardennes','Ariège','Aube','Aude','Aveyron','Bouches-du-Rhône','Calvados','Cantal','Charente','Charente-Maritime','Cher','Corrèze','Corse',"Côte-d'Or","Côtes d'Armor",'Creuse','Dordogne','Doubs','Drôme','Eure','Eure-et-Loire','Finistère','Gard','Haute-Garonne','Gers','Gironde','Hérault','île-et-vilaine','Indre','Indre-et-Loire','Isère','Jura','Landres','Loir-et-Cher','Loire','Haute-Loire','Loire-Atlantique','Loiret','Lot','Lot-et-Garonne','Lozère','Maine-et-Loire','Manche','Marne','Haute-Marne','Mayenne','Meurthe-et-Moselle','Meuse','Morbihan','Moselle','Nièvre','Nord','Oise','Orne','Pas-de-Calais','Puy-de-Dôme','Pyrénées-Atlantique','Hautes-Pyrénées','Pyrénées-Orientales','Bas-Rhin','Haut-Rhin','Rhône','Haute-Saône','Saône-et-Loire','Sarthe','Savoie','Haute-Savoie','Paris','Seine-Maritime','Seine-et-Marne','Yvelines','Deux-Sèvres','Somme','Tarn','Tarn-et-Garonne','Var','Vaucluse','Vendée','Vienne','Haute-Vienne','Vosges','Yonne','Territoire-de-Belfort','Essone','Hauts-de-Seine','Seine-Saint-Denis','Val-de-Marne',"Val-d'Oise"], 'Consommation (MWh)':somme_conso(data_2018)}
    df_2018 = pd.DataFrame(data_final)

    data_final = {'Num_dept':dept_num(),'Nom_dept':['Ain','Aisne','Allier','Alpes de Haute-Provence','Hautes-Alpes','Alpes-Maritimes','Ardêche','Ardennes','Ariège','Aube','Aude','Aveyron','Bouches-du-Rhône','Calvados','Cantal','Charente','Charente-Maritime','Cher','Corrèze','Corse',"Côte-d'Or","Côtes d'Armor",'Creuse','Dordogne','Doubs','Drôme','Eure','Eure-et-Loire','Finistère','Gard','Haute-Garonne','Gers','Gironde','Hérault','île-et-vilaine','Indre','Indre-et-Loire','Isère','Jura','Landres','Loir-et-Cher','Loire','Haute-Loire','Loire-Atlantique','Loiret','Lot','Lot-et-Garonne','Lozère','Maine-et-Loire','Manche','Marne','Haute-Marne','Mayenne','Meurthe-et-Moselle','Meuse','Morbihan','Moselle','Nièvre','Nord','Oise','Orne','Pas-de-Calais','Puy-de-Dôme','Pyrénées-Atlantique','Hautes-Pyrénées','Pyrénées-Orientales','Bas-Rhin','Haut-Rhin','Rhône','Haute-Saône','Saône-et-Loire','Sarthe','Savoie','Haute-Savoie','Paris','Seine-Maritime','Seine-et-Marne','Yvelines','Deux-Sèvres','Somme','Tarn','Tarn-et-Garonne','Var','Vaucluse','Vendée','Vienne','Haute-Vienne','Vosges','Yonne','Territoire-de-Belfort','Essone','Hauts-de-Seine','Seine-Saint-Denis','Val-de-Marne',"Val-d'Oise"], 'Consommation (MWh)':somme_conso(data_2019)}
    df_2019 = pd.DataFrame(data_final)

    data_final = {'Num_dept':dept_num(),'Nom_dept':['Ain','Aisne','Allier','Alpes de Haute-Provence','Hautes-Alpes','Alpes-Maritimes','Ardêche','Ardennes','Ariège','Aube','Aude','Aveyron','Bouches-du-Rhône','Calvados','Cantal','Charente','Charente-Maritime','Cher','Corrèze','Corse',"Côte-d'Or","Côtes d'Armor",'Creuse','Dordogne','Doubs','Drôme','Eure','Eure-et-Loire','Finistère','Gard','Haute-Garonne','Gers','Gironde','Hérault','île-et-vilaine','Indre','Indre-et-Loire','Isère','Jura','Landres','Loir-et-Cher','Loire','Haute-Loire','Loire-Atlantique','Loiret','Lot','Lot-et-Garonne','Lozère','Maine-et-Loire','Manche','Marne','Haute-Marne','Mayenne','Meurthe-et-Moselle','Meuse','Morbihan','Moselle','Nièvre','Nord','Oise','Orne','Pas-de-Calais','Puy-de-Dôme','Pyrénées-Atlantique','Hautes-Pyrénées','Pyrénées-Orientales','Bas-Rhin','Haut-Rhin','Rhône','Haute-Saône','Saône-et-Loire','Sarthe','Savoie','Haute-Savoie','Paris','Seine-Maritime','Seine-et-Marne','Yvelines','Deux-Sèvres','Somme','Tarn','Tarn-et-Garonne','Var','Vaucluse','Vendée','Vienne','Haute-Vienne','Vosges','Yonne','Territoire-de-Belfort','Essone','Hauts-de-Seine','Seine-Saint-Denis','Val-de-Marne',"Val-d'Oise"], 'Consommation (MWh)':somme_conso(data_2020)}
    df_2020 = pd.DataFrame(data_final)

    data_final = {'Num_dept':dept_num(),'Nom_dept':['Ain','Aisne','Allier','Alpes de Haute-Provence','Hautes-Alpes','Alpes-Maritimes','Ardêche','Ardennes','Ariège','Aube','Aude','Aveyron','Bouches-du-Rhône','Calvados','Cantal','Charente','Charente-Maritime','Cher','Corrèze','Corse',"Côte-d'Or","Côtes d'Armor",'Creuse','Dordogne','Doubs','Drôme','Eure','Eure-et-Loire','Finistère','Gard','Haute-Garonne','Gers','Gironde','Hérault','île-et-vilaine','Indre','Indre-et-Loire','Isère','Jura','Landres','Loir-et-Cher','Loire','Haute-Loire','Loire-Atlantique','Loiret','Lot','Lot-et-Garonne','Lozère','Maine-et-Loire','Manche','Marne','Haute-Marne','Mayenne','Meurthe-et-Moselle','Meuse','Morbihan','Moselle','Nièvre','Nord','Oise','Orne','Pas-de-Calais','Puy-de-Dôme','Pyrénées-Atlantique','Hautes-Pyrénées','Pyrénées-Orientales','Bas-Rhin','Haut-Rhin','Rhône','Haute-Saône','Saône-et-Loire','Sarthe','Savoie','Haute-Savoie','Paris','Seine-Maritime','Seine-et-Marne','Yvelines','Deux-Sèvres','Somme','Tarn','Tarn-et-Garonne','Var','Vaucluse','Vendée','Vienne','Haute-Vienne','Vosges','Yonne','Territoire-de-Belfort','Essone','Hauts-de-Seine','Seine-Saint-Denis','Val-de-Marne',"Val-d'Oise"], 'Consommation (MWh)':somme_conso(data_2021)}
    df_2021 = pd.DataFrame(data_final)


    #Visualisation de la carte
    app = Dash(__name__)


    app.layout = html.Div([
        html.H4("Average electricity consumption(MWh) in France"),
        html.P("Select a Year and Details:"),
        dcc.Dropdown(
            options = ['2018','2019', '2020', '2021'], 
            value = '2018', 
            id='candidate'),
        html.Div(id='dd-output-container'),
        dcc.RadioItems(
                    id='candidate2',
                    options = ["Departement", "Commune"],
                    value = "Departement",
                    inline=True
                )
        ,dcc.Graph(id="graph",style={'width': '200vh', 'height': '90vh'}),
        dcc.Graph(id='bar-graph'),
    ])


    @app.callback(
        Output('graph', 'figure'),
        Input('candidate', 'value'),
        Input('candidate2', 'value'))
    def display_choropleth(candidate,candidate2):
        if candidate2== "Commune":
            if candidate=='2018':
                df = data_2018
                Map = json.load(open("./predivis/data/communes-fin.geojson", "r"))
                state_id_map = {}
                for feature in Map["features"]:
                    feature["id"] = feature["properties"]["code"]
                    state_id_map[feature["properties"]["nom"]] = feature["id"]
                fig = px.choropleth_mapbox(
                    df,
                    locations="Num_dept",
                    geojson=Map,
                    color="Consommation (MWh)",
                    hover_name="nom",
                    hover_data=["Consommation (MWh)"],
                    title="Carte de la consommation (MWh) par commune en 2018",
                    mapbox_style="carto-positron",
                    center={"lat": 47, "lon": 2},
                    zoom=4,
                    opacity=0.5
                )
                return fig
            else:
                if candidate=='2019':
                    df = data_2019
                    Map = json.load(open("./predivis/data/communes-fin.geojson", "r"))
                    state_id_map = {}
                    for feature in Map["features"]:
                        feature["id"] = feature["properties"]["code"]
                        state_id_map[feature["properties"]["nom"]] = feature["id"]
                    fig = px.choropleth_mapbox(
                        df,
                        locations="Num_dept",
                        geojson=Map,
                        color="Consommation (MWh)",
                        hover_name="nom",
                        hover_data=["Consommation (MWh)"],
                        title="Carte de la consommation (MWh) par commune en 2019",
                        mapbox_style="carto-positron",
                        center={"lat": 47, "lon": 2},
                        zoom=4,
                        opacity=0.5
                    )
                    return fig
                else :
                    if candidate=='2020':
                        df = data_2020
                        Map = json.load(open("./predivis/data/communes-fin.geojson", "r"))
                        state_id_map = {}
                        for feature in Map["features"]:
                            feature["id"] = feature["properties"]["code"]
                            state_id_map[feature["properties"]["nom"]] = feature["id"]
                        fig = px.choropleth_mapbox(
                            df,
                            locations="Num_dept",
                            geojson=Map,
                            color="Consommation (MWh)",
                            hover_name="nom",
                            hover_data=["Consommation (MWh)"],
                            title="Carte de la consommation (MWh) par commune en 2020",
                            mapbox_style="carto-positron",
                            center={"lat": 47, "lon": 2},
                            zoom=4,
                            opacity=0.5
                        )
                        return fig
                    else :
                        df = data_2021
                        Map = json.load(open("./predivis/data/communes-fin.geojson", "r"))
                        state_id_map = {}
                        for feature in Map["features"]:
                            feature["id"] = feature["properties"]["code"]
                            state_id_map[feature["properties"]["nom"]] = feature["id"]
                        fig = px.choropleth_mapbox(
                            df,
                            locations="Num_dept",
                            geojson=Map,
                            color="Consommation (MWh)",
                            hover_name="nom",
                            hover_data=["Consommation (MWh)"],
                            title="Carte de la consommation (MWh) par commune en 2021",
                            mapbox_style="carto-positron",
                            center={"lat": 47, "lon": 2},
                            zoom=4,
                            opacity=0.5
                        )
                        return fig
        else:
            if candidate=='2018':
                df = df_2018
                Map = json.load(open("./predivis/data/departements.geojson", "r"))
                state_id_map = {}
                for feature in Map["features"]:
                    feature["id"] = feature["properties"]["code"]
                    state_id_map[feature["properties"]["nom"]] = feature["id"]
                fig = px.choropleth_mapbox(
                    df,
                    locations="Num_dept",
                    geojson=Map,
                    color="Consommation (MWh)",
                    hover_name="Nom_dept",
                    hover_data=["Consommation (MWh)"],
                    title="Carte de la consommation (MWh) par departement en 2018",
                    mapbox_style="carto-positron",
                    center={"lat": 47, "lon": 2},
                    zoom=4,
                    opacity=0.5
                )
                return fig
            else:
                if candidate=='2019':
                    df = df_2019
                    Map = json.load(open("./predivis/data/departements.geojson", "r"))
                    state_id_map = {}
                    for feature in Map["features"]:
                        feature["id"] = feature["properties"]["code"]
                        state_id_map[feature["properties"]["nom"]] = feature["id"]
                    fig = px.choropleth_mapbox(
                        df,
                        locations="Num_dept",
                        geojson=Map,
                        color="Consommation (MWh)",
                        hover_name="Nom_dept",
                        hover_data=["Consommation (MWh)"],
                        title="Carte de la consommation (MWh) par departement en 2019",
                        mapbox_style="carto-positron",
                        center={"lat": 47, "lon": 2},
                        zoom=4,
                        opacity=0.5
                    )
                    return fig
                else :
                    if candidate=='2020':
                        df = df_2020
                        Map = json.load(open("./predivis/data/departements.geojson", "r"))
                        state_id_map = {}
                        for feature in Map["features"]:
                            feature["id"] = feature["properties"]["code"]
                            state_id_map[feature["properties"]["nom"]] = feature["id"]
                        fig = px.choropleth_mapbox(
                            df,
                            locations="Num_dept",
                            geojson=Map,
                            color="Consommation (MWh)",
                            hover_name="Nom_dept",
                            hover_data=["Consommation (MWh)"],
                            title="Carte de la consommation (MWh) par departement en 2020",
                            mapbox_style="carto-positron",
                            center={"lat": 47, "lon": 2},
                            zoom=4,
                            opacity=0.5
                        )
                        return fig
                    else :
                        df = df_2021
                        Map = json.load(open("./predivis/data/departements.geojson", "r"))
                        state_id_map = {}
                        for feature in Map["features"]:
                            feature["id"] = feature["properties"]["code"]
                            state_id_map[feature["properties"]["nom"]] = feature["id"]
                        fig = px.choropleth_mapbox(
                            df,
                            locations="Num_dept",
                            geojson=Map,
                            color="Consommation (MWh)",
                            hover_name="Nom_dept",
                            hover_data=["Consommation (MWh)"],
                            title="Carte de la consommation (MWh) par departement en 2021",
                            mapbox_style="carto-positron",
                            center={"lat": 47, "lon": 2},
                            zoom=4,
                            opacity=0.5
                        )
                        return fig

    @app.callback(
        Output('bar-graph', 'figure'),
        Input('candidate', 'value'))
    def display_bar(candidate):
        if candidate == '2018':
            fig2 = px.bar(df_2018, x='Num_dept', y='Consommation (MWh)',title="Histogramme de la consommation(MWh) moyenne par département en 2018")
            return fig2
        else:
            if candidate == '2019':
                fig2 = px.bar(df_2019, x='Num_dept', y='Consommation (MWh)',title="Histogramme de la consommation(MWh) moyenne par département en 2019")
                return fig2
            else:
                if candidate == '2020':
                    fig2 = px.bar(df_2020, x='Num_dept', y='Consommation (MWh)',title="Histogramme de la consommation(MWh) moyenne par département en 2020")
                    return fig2
                else:
                    fig2 = px.bar(df_2021, x='Num_dept', y='Consommation (MWh)',title="Histogramme de la consommation(MWh) moyenne par département en 2021")
                    return fig2

    app.run_server(debug=True)
    return 1