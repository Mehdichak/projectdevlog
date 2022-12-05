# Partie Visualisation du projet :

Cette partie est divisée en trois programmes, ces programmes ont pour objectif de cartographier la consommation d'éléctricité moyenne en MWh avec plus ou moins de détails.

## Visu_commune.py :

Ce programme est le plus complet disponible, il permet de créer une carte de la consommation avec une possibilité de selection de l'année entre les 4 disponibles, et un découpage soit en région soit en département. Un histogramme est en plus affiché pour visualiser les consommations de chaque département par année. 

__Note :__ Le programme fonctionne avec le module Dash qui créer un lien local lors de l'execution du programme, ouvrir ce lien sur un navigateur pour accèder à la visualisation lors de l'execution du programme (un rafraichissement de la page peut être nécéssaire pour afficher les données). La représentation par commune met environ 1 minutes à s'afficher en vu de la quantité de données à traiter. 

## Visu_complet.py :

Ce programme permet d'afficher  une carte de la consommation moyenne (MWh) par année avec un découpage par département. 

__Note :__ Le programme fonctionne avec le module Dash qui créer un lien local lors de l'execution du programme, ouvrir ce lien sur un navigateur pour accèder à la visualisation lors de l'execution du programme (un rafraichissement de la page peut être nécéssaire pour afficher les données).

## data_visu.py :

Ce programme permet d'afficher chaque carte de consommation moyenne par année dans quatres onglets local séparés. 

__Note :__ un rafraichissement de l'onglet peut être nécessaire si le chargement d'un onglet se bloque lors du lancement du programme. 
