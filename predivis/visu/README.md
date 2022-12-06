# Partie Visualisation du projet :

Cette partie est divisée en trois programmes, ces programmes ont pour objectif de cartographier la consommation d'électricité moyenne en MWh avec plus ou moins de détails. Les données utilisées sont stockées dans le dossier Data pour les données de consommation et les fichiers de cartes découpées en départements ou en commune. La fonction min_max est une fonction utilisant le principe des classes pour donner les consommations maximum et minimum du département donné en entrée. 

## Visu_commune.py :

Ce programme est le plus complet disponible, il permet de créer une carte de la consommation avec une possibilité de sélection de l'année entre les 4 disponibles, et un découpage soit en commune soit en département. Un histogramme est en plus affiché pour visualiser les consommations de chaque département par année. 

__Note :__ Le programme fonctionne avec le module Dash qui créer un lien local lors de l'exécution du programme, ouvrir ce lien sur un navigateur permet d'accéder à la visualisation lors de l'exécution du programme (un rafraichissement de la page peut être nécessaire pour afficher les données). Le programme met 15 secondes pour générer le lien local, et le lien local fonctionne véritablement 26 secondes après le lancement du programme. La sélection d'années sur le site quand l'option département est sélectionnée met 2 secondes de chargement. La sélection d'années sur le site, quand l'option commune est sélectionnée, mets 24 secondes. 


## Visu_complet.py :

Ce programme permet d'afficher  une carte de la consommation moyenne (MWh) par année avec un découpage par département. 

__Note :__ Le programme fonctionne avec le module Dash qui créer un lien local lors de l'execution du programme, ouvrir ce lien sur un navigateur pour accèder à la visualisation lors de l'execution du programme (un rafraichissement de la page peut être nécéssaire pour afficher les données). Le programme met 15 secondes pour générer le lien local, et le lien local fonctionne véritablement 26 secondes après le lancement du programme. La sélection d'années sur le site met 2 secondes. 

## data_visu.py :

Ce programme permet d'afficher une carte de consommation moyenne par année dans quatres onglets local séparés. 

__Note :__ Un rafraîchissement de l'onglet peut être nécessaire si le chargement d'un onglet se bloque lors du lancement du programme. Le programme met 20 secondes pour générer les 4 onglets de cartes. 

## Sources :

Les données de consommation proviennent du site : [https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/information/](https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/information/).

Les données de Cartographie proviennent du site : [https://france-geojson.gregoiredavid.fr/](https://france-geojson.gregoiredavid.fr/)
