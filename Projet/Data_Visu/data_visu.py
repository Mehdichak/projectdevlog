import pandas as pd
import json
import numpy as np
import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'browser'

data_2018 = pd.read_csv("./Data_Visu/Conso2018.csv", sep=';')
data_2019 = pd.read_csv("./Data_Visu/Conso2019.csv", sep=';')
data_2020 = pd.read_csv("./Data_Visu/Conso2020.csv", sep=';')
data_2021 = pd.read_csv("./Data_Visu/Conso2021.csv", sep=';')


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
data_2018['Departement'] = data_2018['Departement'].apply(lambda x: str(x) if x > 9999 else "0" + str(x))
data_2018['Departement'] = data_2018['Departement'].apply(lambda x: int(str(x)[:-3]))

data_2019['Departement'] = data_2019['Departement'].apply(lambda x: str(x) if x > 9999 else "0" + str(x))
data_2019['Departement'] = data_2019['Departement'].apply(lambda x: int(str(x)[:-3]))

data_2020['Departement'] = data_2020['Departement'].apply(lambda x: str(x) if x > 9999 else "0" + str(x))
data_2020['Departement'] = data_2020['Departement'].apply(lambda x: int(str(x)[:-3]))

data_2021['Departement'] = data_2021['Departement'].apply(lambda x: str(x) if x > 9999 else "0" + str(x))
data_2021['Departement'] = data_2021['Departement'].apply(lambda x: int(str(x)[:-3]))

#Création de la Carte de France
Map = json.load(open("./Data_Visu/departements.geojson", "r"))
state_id_map = {}
for feature in Map["features"]:
    feature["id"] = feature["properties"]["code"]
    state_id_map[feature["properties"]["nom"]] = feature["id"]

#Figure de la consommation en 2018
fig_2018 = px.choropleth_mapbox(
    data_2018,
    locations="Departement",
    geojson=Map,
    color="consommation",
    hover_name="Departement",
    hover_data=["consommation"],
    title="Consommation",
    mapbox_style="carto-positron",
    center={"lat": 47, "lon": 2},
    zoom=4,
    opacity=0.5,
)
fig_2018.show()

#Figure de la consommation en 2019
fig_2019 = px.choropleth_mapbox(
    data_2019,
    locations="Departement",
    geojson=Map,
    color="consommation",
    hover_name="Departement",
    hover_data=["consommation"],
    title="Consommation",
    mapbox_style="carto-positron",
    center={"lat": 47, "lon": 2},
    zoom=4,
    opacity=0.5,
)
fig_2019.show()

#Figure de la consommation en 2020
fig_2020 = px.choropleth_mapbox(
    data_2020,
    locations="Departement",
    geojson=Map,
    color="consommation",
    hover_name="Departement",
    hover_data=["consommation"],
    title="Consommation",
    mapbox_style="carto-positron",
    center={"lat": 47, "lon": 2},
    zoom=4,
    opacity=0.5,
)
fig_2020.show()

#Figure de la consommation en 2021
fig_2021 = px.choropleth_mapbox(
    data_2021,
    locations="Departement",
    geojson=Map,
    color="consommation",
    hover_name="Departement",
    hover_data=["consommation"],
    title="Consommation",
    mapbox_style="carto-positron",
    center={"lat": 47, "lon": 2},
    zoom=4,
    opacity=0.5,
)
fig_2021.show()