import pandas as pd
import numpy as np

from datetime import datetime, timedelta, timezone
from prophet.serialize import model_to_json, model_from_json
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.api import ExponentialSmoothing, Holt
from prophet import Prophet
from datetime import datetime, timedelta, timezone

import matplotlib.pyplot as plt
#plt.style.use('fivethirtyeight')

# lecture du fichier csv (a remplacer par le lien !!!)


#fonction prepare data 
def prepare_data(filepath="PredictionCleanData.csv", date_initiale='2022-09-24', methode='Prophet', source_conso="Consommation (MW)"):
    """ Fonction qui traite les données pour entraîner le modèle. 
    
    Cette fonction met les données au format attendu par le modèle utilisé.
    
    Inputs :
        - filepath (str): Tableau de données initial obtenu à partir du lien. 
        - data_initiale (str): Date à partir de laquelle le modèle s'entraîne sur les données. Le format doit être "%Y-%m-%d".
        - methode (str): Méthode à utiliser pour la prédiction ("Prophet" ou "Holt_Winters")
        - source_conso (str): Grandeur à prédire. 

    outputs:
        - df_data (pd.DataFrame): Données traitées à fournir au modèle.
        
    """
    df_data=pd.read_csv(filepath, sep=";")
    # Enlever les lignes où il manque des informations
    df_data.dropna(subset=[source_conso], inplace = True)  
    # Dupliquer la colonne indiquant les date
    df_data['Time'] = df_data["Date - Heure"] 
    # Convertir les colonnes au format datetime 
    df_data['Time']=pd.to_datetime(df_data['Time'])
    df_data["Date - Heure"]=pd.to_datetime(df_data["Date - Heure"])
    df_data.set_index("Date - Heure", inplace=True)
    if methode=="Prophet":
        # Pour cette méthode, le dataframe doit avoir un format particulier
        df_data=df_data[['Time',source_conso]]
        df_data=df_data[date_initiale:"2022-12-06"]
        # Rename columns for Prophet forecasting methods
        #la methode prophet requiert un changement des noms des colonnes en ds et y
        #la colonne time ne doit pas etre en index 
        df_data = df_data.rename(columns={'Time': 'ds', source_conso: 'y'})
        # Reset_index
        df_data.reset_index(inplace=True, drop=True)
    elif methode=="Holt_Winters":
        # Sorting df_data chronologically
        df_data=df_data.sort_index(ascending=True)
        
        #condition garder la ligne de la date du debut d'entrainement 
        df_data=df_data[date_initiale:"2022-12-06"] 
        df_data=df_data[[source_conso]]
    return df_data


def predict_for_day(filepath="PredictionCleanData.csv",filepath_out="prediction.csv", date_initiale='2021-12-07', methode='Prophet', source_conso="Consommation (MW)", date_prediction='2022-12-08', save_model=False, load_model=False):
    """ Fonction qui prédit pour un jour donné les données de consommation souhaitées.
    
    Inputs :
        - filepath (str): Chemin d'accès du fichier contenant les données nécessaires à la prédiction.
        - filepath_out (str): Chemin d'accès du fichier CSV des données prédites
        - data_initiale (str): Date à partir de laquelle le modèle s'entraîne sur les données. Le format doit être "%Y-%m-%d".
        - methode (str): Méthode à utiliser pour la prédiction ("Prophet" ou "Holt_Winters")
        - source_conso (str): Grandeur à prédire. 
        - date_prediction (str): Date de la consommation à prédire. Le format doit être "%Y-%m-%d".
        - save_model (bool): si True, enregistre le modèle dans le dossier actuel sous format JSON.
        - load_model (bool): si True, récupère le modèle enregistré dans le dossier actuel sous format JSON.
          ne fonctionne que s'il y a deja un modèle enregistré. (que pour la methode prophet)

    Outputs: 
        - predictions (pd.DataFrame): Prédictions pour la grandeur choisie.
        - Un fichier CSV contenant les données prédites
    """
    # Préparer les données via fonctions imbriquées 
    transformed_data= prepare_data(filepath=filepath, date_initiale=date_initiale, methode=methode, source_conso=source_conso)
    # Entrainer le modèle 
    if methode=="Prophet":
        if load_model :
            #permet de telecharger le modele preentrainé pour l'utiliser directement dans la prediction
            # a ne pas utiliser si il ny a pas de modele entrainé (par default en false ) 
            with open('serialized_model.json', 'r') as fin:
                model = model_from_json(fin.read())  # Load model
        else :
            #reentrainer le modele 
            model = Prophet(interval_width=0.95)
            #pour chercher les parametres 
            model.fit(transformed_data)
        if save_model :
            #telecharge le modele entraine sur l'ordi afin d'etre plus rapide a executer (par defaut false)
            with open('serialized_model.json', 'w') as fout:
                fout.write(model_to_json(model))  # Save model
        # Définition de la période à prédire
        #pour le fct des des modeles on a besoin d'une periode de prediction *
        #pour eviter de devoir changer la periode a predire donc il calcule automatiquement le nbr de jours 
        # entre la date de fin dentrainement et la date a predire puis la convertir en nbre de quarts d'heure
        #pour savoir jusqu'a quand predire 
        #date_pred = datetime.strptime(date_prediction, "%Y-%m-%d")
        date_pred = pd.to_datetime(date_prediction)
        date_finale = transformed_data["ds"].values[-1]
        jours=(date_pred-date_finale).days + 2
        period_to_forecast= jours*96
        #fonction future du package prophet qui prepare le tableau de prediction (output)
        future_dates = model.make_future_dataframe(periods=period_to_forecast, freq='15min')
        # Prédiction
        forecast = model.predict(future_dates)[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
        #recuperer les lignes du tableau correpondante au jour de prediction 
        resultat=forecast[(forecast['ds']>=date_prediction)&(forecast['ds']<(date_pred + timedelta(days=1)))]
        # Visualisation des résultats 
        #comparaisons des prediction et des valeurs reelles . 
        fig=model.plot(forecast[forecast['ds']<(date_pred + timedelta(days=10))], uncertainty=True,  xlabel='Date', ylabel=source_conso)
        ax = fig.gca()
        ax.set_title("évolution de "+source_conso, size=20)
        ax.set_xlabel("Date", size=15)
        ax.set_ylabel(source_conso, size=15)
        ax.tick_params(axis="x", labelsize=10)
        ax.tick_params(axis="y", labelsize=10)
        plt.show()
        resultat = pd.DataFrame(resultat)
        resultat = resultat[["ds","yhat"]]
        resultat.to_csv(filepath_out)
        print("Resultat téléchargé intégré au fichier"+filepath_out)
    elif methode=="Holt_Winters":
        model = ExponentialSmoothing(transformed_data, seasonal_periods=4*24*7, trend='add', seasonal='add', use_boxcox=True).fit()
        date_pred = pd.to_datetime(date_prediction)
        # ona observé une saisinalité de 1jour ou d'une semaine
        print(date_pred)
        date_finale = transformed_data.tail(1).index.item().to_pydatetime()
        print(date_finale)
        jours=(date_pred-date_finale).days + 1
        print(jours)
        period_to_forecast= jours*96
        fcast =model.forecast(period_to_forecast).rename('Additive')
        print(fcast)
        resultat=fcast[:672]
        resultat = pd.DataFrame(resultat)
        resultat.to_csv(filepath_out)
        print("Resultat téléchargé intégré au fichier"+filepath_out)
    else : 
        print("Méthode non reconnue")
   
    return resultat



predict_for_day(filepath="PredictionCleanData.csv",filepath_out="prediction3.csv", date_initiale='2021-12-07', methode='Prophet', source_conso="Consommation (MW)", date_prediction='2022-12-07', save_model=False, load_model=False)