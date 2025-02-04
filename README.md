# Téléchargeur YouTube en Arabe

Ce projet propose une application Python avec une interface graphique (Tkinter) en arabe qui vous permet de télécharger un extrait (défini par un intervalle de temps) d'une vidéo YouTube en utilisant pytube.

## Fonctionnalités

- Téléchargement d'un extrait vidéo : Spécifiez l'URL de la vidéo, le temps de début et le temps de fin (en minutes) pour extraire la portion souhaitée.
- Interface Graphique en arabe : Utilisation de Tkinter pour une prise en main simple et intuitive.
- Sélection du répertoire de sortie : Un bouton "????" permet de définir l'emplacement du fichier de sortie.

## Prérequis

- Python 3 ou supérieur.
- pytube (installé via le fichier requirements.txt)
- Tkinter est inclus avec Python sur de nombreuses distributions.

## Installation

Cloner le dépôt :

git clone https://github.com/votre-utilisateur/arabic-youtube-downloader.git
cd arabic-youtube-downloader

(Optionnel) Créer et activer un environnement virtuel :

python -m venv venv
source venv/bin/activate  # Pour Windows : venv\Scripts\activate

Installer les dépendances :

pip install -r requirements.txt

## Utilisation

Exécutez le script principal :

python arabyoutubeclipdownloader.py

Dans la fenêtre qui s'ouvre :
1. Collez l'URL de la vidéo YouTube
2. Entrez le temps de début en minutes
3. Entrez le temps de fin en minutes
4. Choisissez l'emplacement de sauvegarde avec le bouton "????"
5. Cliquez sur "?????" pour démarrer le téléchargement

## Code Source