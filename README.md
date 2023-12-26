# Projet 4 Développeur d'application Python : programmation orientée objet


## Informations générales

Ce projet constitue un examen dans le cadre du parcours Développeur d'application Python d'OpenClassrooms, il est codé avec le langage Python.
Concrètement, il consiste à créer un programme permettant de faire fonctionner des tournois d'échecs.

## Auteur

Fabien ROYER

## Contributions

Le projet est achevé depuis novembre 2023.

## Installation

Création de l'environnement :
python -m venv env

Lancement de l'environnement :
env\Scripts\activate

Utilisez le _package installer_ [pip](https://pypi.org/project/pip/) pour installer les packages inclus dans le fichier requirements.txt, pour cela utilisez dans le terminal la commande :
```bash
pip install -r requirements.txt
```

## Utilisation

Pour exécuter le code, le point d'entrée étant le fichier main.py, il faut entrer la commande suivante dans le terminal :
```bash
python main.py
```

Ce programme permet à un utilisateur d'enregistrer des joueurs et des tournois d'échecs, de gérer le déroulé d'un tournoi de quatre rounds et de consulter les données enregistrées.
Pour faire fonctionner un tournoi, l'utilisateur doit sélectionner huit joueurs. Le programme sélectionnera automatiquement les joueurs qui s'affronteront pour chaque round selon le système suisse, l'utilisateur devra uniquement indiquer que le round est terminé et renseigner le score de joueur. Il est également possible de consulter directement la liste des joueurs, la liste des tournois ainsi que le résultat des rounds.

