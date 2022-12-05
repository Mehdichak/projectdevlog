import pandas as pd
import json
import numpy as np
import plotly.express as px
import plotly.io as pio
from dash import Dash, dcc, html, Input, Output

def somme_conso(x):
    i=0
    m=[]
    for i in range(95):
        datatemp = x[ x["Departement"] == i+1 ]
        Total = datatemp['consommation'].sum()
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

pio.renderers.default = 'browser'

#Chargement des données
data_2018 = pd.read_csv("./Projet/Data_Visu/Data/Conso2018.csv", sep=';')
data_2019 = pd.read_csv("./Projet/Data_Visu/Data/Conso2019.csv", sep=';')
data_2020 = pd.read_csv("./Projet/Data_Visu/Data/Conso2020.csv", sep=';')
data_2021 = pd.read_csv("./Projet/Data_Visu/Data/Conso2021.csv", sep=';')

#Nettoyage des données
data_2018.drop_duplicates(inplace=True)
data_2018.dropna(inplace=True)
data_2018 = data_2018.rename(columns={"Code INSEE de la commune": "Departement", "Nom de la commune": "nom",
                        "Consommation annuelle moyenne de la commune (MWh)": "consommation"})
data_2019.drop_duplicates(inplace=True)
data_2019.dropna(inplace=True)
data_2019 = data_2019.rename(columns={"Code INSEE de la commune": "Departement", "Nom de la commune": "nom",
                        "Consommation annuelle moyenne de la commune (MWh)": "consommation"})
data_2020.drop_duplicates(inplace=True)
data_2020.dropna(inplace=True)
data_2020 = data_2020.rename(columns={"Code INSEE de la commune": "Departement", "Nom de la commune": "nom",
                        "Consommation annuelle moyenne de la commune (MWh)": "consommation"})
data_2021.drop_duplicates(inplace=True)
data_2021.dropna(inplace=True)
data_2021 = data_2021.rename(columns={"Code INSEE de la commune": "Departement", "Nom de la commune": "nom",
                        "Consommation annuelle moyenne de la commune (MWh)": "consommation"})


#Transformation des codes insee en numéro de département
data_2018['Departement'] = data_2018['Departement'].apply(lambda x: int(str(x)[:-3]))

data_2019['Departement'] = data_2019['Departement'].apply(lambda x: int(str(x)[:-3]))

data_2020['Departement'] = data_2020['Departement'].apply(lambda x: int(str(x)[:-3]))

data_2021['Departement'] = data_2021['Departement'].apply(lambda x: int(str(x)[:-3]))

#Data des sommes de consommation par département
data_final = {'Numero':dept_num(),'Nom_dept':['Ain','Aisne','Allier','Alpes de Haute-Provence','Hautes-Alpes','Alpes-Maritimes','Ardêche','Ardennes','Ariège','Aube','Aude','Aveyron','Bouches-du-Rhône','Calvados','Cantal','Charente','Charente-Maritime','Cher','Corrèze','Corse',"Côte-d'Or","Côtes d'Armor",'Creuse','Dordogne','Doubs','Drôme','Eure','Eure-et-Loire','Finistère','Gard','Haute-Garonne','Gers','Gironde','Hérault','île-et-vilaine','Indre','Indre-et-Loire','Isère','Jura','Landres','Loir-et-Cher','Loire','Haute-Loire','Loire-Atlantique','Loiret','Lot','Lot-et-Garonne','Lozère','Maine-et-Loire','Manche','Marne','Haute-Marne','Mayenne','Meurthe-et-Moselle','Meuse','Morbihan','Moselle','Nièvre','Nord','Oise','Orne','Pas-de-Calais','Puy-de-Dôme','Pyrénées-Atlantique','Hautes-Pyrénées','Pyrénées-Orientales','Bas-Rhin','Haut-Rhin','Rhône','Haute-Saône','Saône-et-Loire','Sarthe','Savoie','Haute-Savoie','Paris','Seine-Maritime','Seine-et-Marne','Yvelines','Deux-Sèvres','Somme','Tarn','Tarn-et-Garonne','Var','Vaucluse','Vendée','Vienne','Haute-Vienne','Vosges','Yonne','Territoire-de-Belfort','Essone','Hauts-de-Seine','Seine-Saint-Denis','Val-de-Marne',"Val-d'Oise"], 'Consommation':somme_conso(data_2018)}
df_2018 = pd.DataFrame(data_final)

data_final = {'Numero':dept_num(),'Nom_dept':['Ain','Aisne','Allier','Alpes de Haute-Provence','Hautes-Alpes','Alpes-Maritimes','Ardêche','Ardennes','Ariège','Aube','Aude','Aveyron','Bouches-du-Rhône','Calvados','Cantal','Charente','Charente-Maritime','Cher','Corrèze','Corse',"Côte-d'Or","Côtes d'Armor",'Creuse','Dordogne','Doubs','Drôme','Eure','Eure-et-Loire','Finistère','Gard','Haute-Garonne','Gers','Gironde','Hérault','île-et-vilaine','Indre','Indre-et-Loire','Isère','Jura','Landres','Loir-et-Cher','Loire','Haute-Loire','Loire-Atlantique','Loiret','Lot','Lot-et-Garonne','Lozère','Maine-et-Loire','Manche','Marne','Haute-Marne','Mayenne','Meurthe-et-Moselle','Meuse','Morbihan','Moselle','Nièvre','Nord','Oise','Orne','Pas-de-Calais','Puy-de-Dôme','Pyrénées-Atlantique','Hautes-Pyrénées','Pyrénées-Orientales','Bas-Rhin','Haut-Rhin','Rhône','Haute-Saône','Saône-et-Loire','Sarthe','Savoie','Haute-Savoie','Paris','Seine-Maritime','Seine-et-Marne','Yvelines','Deux-Sèvres','Somme','Tarn','Tarn-et-Garonne','Var','Vaucluse','Vendée','Vienne','Haute-Vienne','Vosges','Yonne','Territoire-de-Belfort','Essone','Hauts-de-Seine','Seine-Saint-Denis','Val-de-Marne',"Val-d'Oise"], 'Consommation':somme_conso(data_2019)}
df_2019 = pd.DataFrame(data_final)

data_final = {'Numero':dept_num(),'Nom_dept':['Ain','Aisne','Allier','Alpes de Haute-Provence','Hautes-Alpes','Alpes-Maritimes','Ardêche','Ardennes','Ariège','Aube','Aude','Aveyron','Bouches-du-Rhône','Calvados','Cantal','Charente','Charente-Maritime','Cher','Corrèze','Corse',"Côte-d'Or","Côtes d'Armor",'Creuse','Dordogne','Doubs','Drôme','Eure','Eure-et-Loire','Finistère','Gard','Haute-Garonne','Gers','Gironde','Hérault','île-et-vilaine','Indre','Indre-et-Loire','Isère','Jura','Landres','Loir-et-Cher','Loire','Haute-Loire','Loire-Atlantique','Loiret','Lot','Lot-et-Garonne','Lozère','Maine-et-Loire','Manche','Marne','Haute-Marne','Mayenne','Meurthe-et-Moselle','Meuse','Morbihan','Moselle','Nièvre','Nord','Oise','Orne','Pas-de-Calais','Puy-de-Dôme','Pyrénées-Atlantique','Hautes-Pyrénées','Pyrénées-Orientales','Bas-Rhin','Haut-Rhin','Rhône','Haute-Saône','Saône-et-Loire','Sarthe','Savoie','Haute-Savoie','Paris','Seine-Maritime','Seine-et-Marne','Yvelines','Deux-Sèvres','Somme','Tarn','Tarn-et-Garonne','Var','Vaucluse','Vendée','Vienne','Haute-Vienne','Vosges','Yonne','Territoire-de-Belfort','Essone','Hauts-de-Seine','Seine-Saint-Denis','Val-de-Marne',"Val-d'Oise"], 'Consommation':somme_conso(data_2020)}
df_2020 = pd.DataFrame(data_final)

data_final = {'Numero':dept_num(),'Nom_dept':['Ain','Aisne','Allier','Alpes de Haute-Provence','Hautes-Alpes','Alpes-Maritimes','Ardêche','Ardennes','Ariège','Aube','Aude','Aveyron','Bouches-du-Rhône','Calvados','Cantal','Charente','Charente-Maritime','Cher','Corrèze','Corse',"Côte-d'Or","Côtes d'Armor",'Creuse','Dordogne','Doubs','Drôme','Eure','Eure-et-Loire','Finistère','Gard','Haute-Garonne','Gers','Gironde','Hérault','île-et-vilaine','Indre','Indre-et-Loire','Isère','Jura','Landres','Loir-et-Cher','Loire','Haute-Loire','Loire-Atlantique','Loiret','Lot','Lot-et-Garonne','Lozère','Maine-et-Loire','Manche','Marne','Haute-Marne','Mayenne','Meurthe-et-Moselle','Meuse','Morbihan','Moselle','Nièvre','Nord','Oise','Orne','Pas-de-Calais','Puy-de-Dôme','Pyrénées-Atlantique','Hautes-Pyrénées','Pyrénées-Orientales','Bas-Rhin','Haut-Rhin','Rhône','Haute-Saône','Saône-et-Loire','Sarthe','Savoie','Haute-Savoie','Paris','Seine-Maritime','Seine-et-Marne','Yvelines','Deux-Sèvres','Somme','Tarn','Tarn-et-Garonne','Var','Vaucluse','Vendée','Vienne','Haute-Vienne','Vosges','Yonne','Territoire-de-Belfort','Essone','Hauts-de-Seine','Seine-Saint-Denis','Val-de-Marne',"Val-d'Oise"], 'Consommation':somme_conso(data_2021)}
df_2021 = pd.DataFrame(data_final)


#Visualisation des cartes
app = Dash(__name__)

app.layout = html.Div([
    html.H4('Consommation moyenne(MWh) par département en fonction du temps'),
    html.P("Select a Year:"),
    dcc.RadioItems(
        id='candidate', 
        options=["2018", "2019", "2020", "2021"],
        value="2018",
        inline=True
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output('graph', 'figure'),
    Input('candidate', 'value'))
def display_choropleth(candidate):
    if candidate=='2018':
        df = df_2018
        Map = json.load(open("./Projet/Data_Visu/Geojson/departements.geojson", "r"))
        state_id_map = {}
        for feature in Map["features"]:
            feature["id"] = feature["properties"]["code"]
            state_id_map[feature["properties"]["nom"]] = feature["id"]
        fig = px.choropleth_mapbox(
            df,
            locations="Numero",
            geojson=Map,
            color="Consommation",
            hover_name="Nom_dept",
            hover_data=["Consommation"],
            title="Consommation par departement en 2018",
            mapbox_style="carto-positron",
            center={"lat": 47, "lon": 2},
            zoom=4,
            opacity=0.5
        )
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        return fig
    else:
        if candidate=='2019':
            df = df_2019
            Map = json.load(open("./Projet/Data_Visu/Geojson/departements.geojson", "r"))
            state_id_map = {}
            for feature in Map["features"]:
                feature["id"] = feature["properties"]["code"]
                state_id_map[feature["properties"]["nom"]] = feature["id"]
            fig = px.choropleth_mapbox(
                df,
                locations="Numero",
                geojson=Map,
                color="Consommation",
                hover_name="Nom_dept",
                hover_data=["Consommation"],
                title="Consommation par departement en 2019",
                mapbox_style="carto-positron",
                center={"lat": 47, "lon": 2},
                zoom=4,
                opacity=0.5
            )
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            return fig
        else :
            if candidate=='2020':
                df = df_2020
                Map = json.load(open("./Projet/Data_Visu/Geojson/departements.geojson", "r"))
                state_id_map = {}
                for feature in Map["features"]:
                    feature["id"] = feature["properties"]["code"]
                    state_id_map[feature["properties"]["nom"]] = feature["id"]
                fig = px.choropleth_mapbox(
                    df,
                    locations="Numero",
                    geojson=Map,
                    color="Consommation",
                    hover_name="Nom_dept",
                    hover_data=["Consommation"],
                    title="Consommation par departement en 2020",
                    mapbox_style="carto-positron",
                    center={"lat": 47, "lon": 2},
                    zoom=4,
                    opacity=0.5
                )
                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                return fig
            else :
                df = df_2021
                Map = json.load(open("./Projet/Data_Visu/Geojson/departements.geojson", "r"))
                state_id_map = {}
                for feature in Map["features"]:
                    feature["id"] = feature["properties"]["code"]
                    state_id_map[feature["properties"]["nom"]] = feature["id"]
                fig = px.choropleth_mapbox(
                    df,
                    locations="Numero",
                    geojson=Map,
                    color="Consommation",
                    hover_name="Nom_dept",
                    hover_data=["Consommation"],
                    title="Consommation par departement en 2021",
                    mapbox_style="carto-positron",
                    center={"lat": 47, "lon": 2},
                    zoom=4,
                    opacity=0.5
                )
                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                return fig





app.run_server(debug=True)