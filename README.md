# Module Predivis

<p align="center" scale=30%>
  <img src="https://github.com/Mehdichak/projectdevlog/blob/main/doc/_images/Logo.png" width=150 title="Logo">
</p>


## But du module
Ce module a pour but d'une part, de représenter la consommation électrique française sur une carte interactive de la France à partir de cette [Base de données](https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/information/), ainsi que de la prédire sur une journée, ceci via cette autre [Base de données](https://odre.opendatasoft.com/explore/dataset/eco2mix-national-tr/information/?disjunctive.nature&sort=-date_heure). Les fonctions sont contenues dans le dossier predivis et la sparation entre visualisation et prediction se fait par les dossiers respectifs au sein du dossier predivis.

## Membres du Groupe

Leroy Nicolas nicolas.leroy@etu.umontpellier.fr

Chakroun Mohamed Mehdi mohamed-mehdi.chakroun@etu.umontpellier.fr

Axel de Montgolfier axel.de-montgolfier@etu.umontpellier.fr

## Utilisation
  - Il est nécessaire pour utiliser les fonctions présentes dans ce module d'instaler les packages présent dans requirements.txt .
  - Afin d'utiliser la fonction de prédiction (```predivis.prediction.prepare_for_day()```), il est nécessaire de télécharger un jeu de donnée au moyen de la fonction ```predivis.prediction.dataloading()```, celui ci sera placé (si vous ne paramétrez pas la fonction) dans le repertoire où est ouvert votre terminal.
  - Les Trois fonctions de visualisation ne sont actuellement accessibles qu'en positionnant le terminal dans le dossier projectdevlog/ .
  - afin d'accéder à la documentation des fonctions , placez vous dans le dossier doc et utilisez ```$ make html```
## Plan

Afin de réaliser nos objectifs, on considère les deux objectifs majeurs, composée des problématiques suivantes :

#### Construire un modèle prédictif

- Nettoyer et prendre en charge la base de données de prédiction
- Imaginer et vérifier mathématiquement l'algorithme predictif
- Mettre en place les tests unitaires
- Implémenter l'algorithme sur python
- Illustrer les données de prédictions
- Mettre en place une documentation

#### Coder une visualisation sur une carte interactive
- Nettoyer et prendre en charge la base de données de visualisation
- Mettre en place des tests unitaires
- Transformer les données en une carte interactive à l'aide de python
- Mettre en place une documentation


Pour réaliser ce projet, nous allons répartir les tâches de la manière suivante : Mehdi et Nicolas s'occuperont de la partie concernant la construction du modèle prédictif et Axel s'occupera de la partie visualisation de la carte interactive. Chacun s'occupera principalement de ses tâches, mais pourra être amené à contribuer sur d'autres taches.



