# Logiciel de tournoi d’échecs
Programme autonome de gestion de tournois d'échecs, qui fonctionne hors ligne et exécutable dans une console.

Le programme utilise la librairie TinyDB pour sauvegarder les joueurs et les tournois.

Il permet de :
- Créer et sauvegarder des joueurs.
- Créer et sauvegarder des tournois.
- Lancer des tournois.
- Arrêter un tournoi en cours et le reprendre plus tard.

## Utilisation
### Prérequis
* Un terminal (par exemple Windows PowerShell)
* Python3 version >= 3.10 (vérifier avec `python -V`)

### 1 - Télécharger les fichiers
* Télécharger le zip depuis le lien: 
[https://github.com/[...]/main.zip](https://github.com/N-Lecl/OCR-Python-4/archive/refs/heads/main.zip)
* Extraire le zip

### 2 - Configurer virtual environment
* Ouvrir un terminal
* Naviguer vers le dossier extrait _([...]\OCR-Python-4-main)_
* Créer un environnement virtuel avec la commande `python -m venv env`
* Activer l'environnement avec `.\env\Scripts\activate` (`source env/bin/activate` sur Linux)
* Installer les packages avec `pip install -r .\requirements.txt`

### 3 - Exécuter le code
* Exécuter le programme avec la commande `py.exe .\main.py`
* Créer d'abord des joueurs (menu 4)
* Créer un nouveau tournoi (menu 1)
* Lancer le nouveau tournoi (menu 2)
* Si un tournoi est arrêté entre 2 tours, il est possible de le sélectionner 
et le continuer (menu 3)

## Rapport flake8

Le repository contient un rapport flake8 dans le dossier _flake8_rapport_, qui n'affiche aucune erreur. 
Il est possible de générer un nouveau rapport avec la commande :
```bash
flake8
```

Le fichier ```.flake8``` à la racine contient les paramètres concernant la génération du rapport.