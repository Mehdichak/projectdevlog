# Partie Prediction du projet :

Cette partie est divisée en deux programmes, ces programmes ont pour objectif de prédire à partir de données historiques de consommation d'électricité (en MWH) en France, la même consommation pour un jour futur choisi par l'utilisateur.

## dataload.py :

Ce programme permet d'obtenir les données à utiliser pour la prédiction sous la forme d'un fichier csv au nom de `PredictionCleanData.csv` . 
__Note :__ Le programme fonctionne en 3 grandes étapes : 

* Récupérer les données brutes (si celles-ci ont été téléchargées avant, elles sont récupérées dans le dossier sinon elles sont téléchargées directement)
* Les données sont nettoyées (enlever les données manquantes, les colonnes superflues, trier les données (index), concaténer les données...)et adaptées à la fonction utilisée ultérieurement 
*  Générer les données préparées pour la prédiction en format csv .




## predict.py :

Ce fichier contient le programme principal qui permet de faire la prédiction pour un jour choisi par l'utilisateur de la consommation de la source choisie selon deux méthodes de prévision différentes. Ce fichier contient deux fonctions : une fonction secondaire `prepare_data` imbriquée dans une fonction principale `predict_for_day` .

__Note :__ Le programme peut faire la prédiction selon deux méthodes différentes : 
* On peut utiliser le modèle `HOLT WINTERS` à travers la méthode `Exponential Smoothing` présente dans le module `statsmodel`
* On peut utiliser la méthode implémentée dans le package `Prophet` de Facebook. 
Les hyper paramètres de ces modèles ont été choisis pendant la phase initiale de recherche du projet et les modèles retenus ont été utilisés directement dans la fonction prédiction.

## Utilisation du programme : 
### Requirements 
Vérifier que les packages sont bien installés dans l'environnement.
* pandas==1.5.1
* numpy==1.23.4
* plotly==5.9.0
* prophet==1.0.1
* statsmodels==0.13.2
* requests==2.28.1

### Via la ligne de commande : 
Il faut d'abord installer le package via pip install :

Pour lacer la prédiction avec la ligne de commande suivante :

Cette méthode ne permet pas de modifier les paramètres du programme (la méthode, la source, la date du début d'entraînement, la date à prédire ...).
###  via execution  :
Lancer `Dataloading.py` pour obtenir le data frame (PredictionCleanData.csv) qui se téléchargera automatiquement et lancer le programme `predict.py`






 

## Sources :

Les données (court terme data) de consommation proviennent du site : [ https://odre.opendatasoft.com/explore/dataset/eco2mix-national-tr/information/?disjunctive.nature&sort=-date_heure).

Les données (long terme data) de consommation proviennent du site : [https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/table/?disjunctive.nature&sort=-date_heure).



