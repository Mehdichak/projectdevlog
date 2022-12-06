# Partie Prediction du projet :

Cette partie est divisée en deux programmes, ces programmes ont pour objectif de prédire à partir de données historiques de consommation d'electricité (en MWH) en France, la même consommation pour un jour futur choisi par l'utilisateur.

## DataLoading.py :

Ce programme permet d'obtenir les données à utiliser pour la prédiction sous la forme d'un fichier csv au nom de `PredictionCleanData.csv` . 
__Note :__ Le programme fonctionne en 3 grandes étapes : 

* Récupérer les données brutes (si celles-ci ont été téléchargées avant, elles sont récupérées dans le dossier sinon elles sont téléchargées directement)
* Les données sont nettoyées (enlever les données manquantes, les colonnes superflues, trier les données (index), concaténer les données...)et adaptées à la fonction utilisée ultérieurement 
*  Générer les données préparées pour la prédiction en format csv .




## Predict.py :

Ce fichier contient le programme principale qui permet de faire la prédiction pour un jour choisi par l'utilisateur de la consommation de la source choisie selon deux methodes de prévisions différentes . Ce fichier contient deux  fonctions : une fonction secondaire `prepare_data` imbriquée dans une fonction principale `predict_for_day` .

__Note :__Le programme peut faire la prédiction selon deux méthodes différentes : 
* On peut utiliser le modéle `HOLT WINTERS` à travers la méthode `Exponential Smoothing` présente dans le module `statsmodel`
* On peut utiliser la methode implémenté dans le package `Prophet` de Facebook. 
Les hyper parametres de ces modéles ont été choisis pendant la phase initiale de recherche du projet et les modéles retenus ont été utilisés directement dans la fonction prediction.

## Utilisation du programme : 
### Requirements 
Verifier que les packages sont bien installés dans l'environnement.
* pandas==1.5.1
* numpy==1.23.4
* plotly==5.9.0
* prophet==1.0.1
* statsmodels==0.13.2
* requests==2.28.1

### Via la ligne de commande : 
Il faut d'abord installer le package via pip install 
```
 {
  
}
```
Pour lacer la prediction avec la ligne de commande suivante 
```
 {
  
}
```
Cette methode ne permet pas de modifier les parametres du programme (la methode , la source , la date du debut d'entrainement, la date a predire ...)
###  via execution  :
Lancer `Dataloading.py` pour obtenir le data frame (PredictionCleanData.csv) qui se telechargera automatiquement et lancer le programme `predict.py`






 

## Sources :

Les données (court terme data) de consommation proviennent du site : [ https://odre.opendatasoft.com/explore/dataset/eco2mix-national-tr/information/?disjunctive.nature&sort=-date_heure).
Les données (long terme data) de consommation proviennent du site : [https://odre.opendatasoft.com/explore/dataset/eco2mix-national-cons-def/table/?disjunctive.nature&sort=-date_heure).



