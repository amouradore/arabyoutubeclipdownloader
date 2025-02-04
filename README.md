# T�l�chargeur YouTube en Arabe

Ce projet propose une application Python avec une interface graphique (Tkinter) en arabe qui vous permet de t�l�charger un extrait (d�fini par un intervalle de temps) d'une vid�o YouTube en utilisant pytube.

## Fonctionnalit�s

- T�l�chargement d'un extrait vid�o : Sp�cifiez l'URL de la vid�o, le temps de d�but et le temps de fin (en minutes) pour extraire la portion souhait�e.
- Interface Graphique en arabe : Utilisation de Tkinter pour une prise en main simple et intuitive.
- S�lection du r�pertoire de sortie : Un bouton "????" permet de d�finir l'emplacement du fichier de sortie.

## Pr�requis

- Python 3 ou sup�rieur.
- pytube (install� via le fichier requirements.txt)
- Tkinter est inclus avec Python sur de nombreuses distributions.

## Installation

Cloner le d�p�t :

git clone https://github.com/votre-utilisateur/arabic-youtube-downloader.git
cd arabic-youtube-downloader

(Optionnel) Cr�er et activer un environnement virtuel :

python -m venv venv
source venv/bin/activate  # Pour Windows : venv\Scripts\activate

Installer les d�pendances :

pip install -r requirements.txt

## Utilisation

Ex�cutez le script principal :

python arabyoutubeclipdownloader.py

Dans la fen�tre qui s'ouvre :
1. Collez l'URL de la vid�o YouTube
2. Entrez le temps de d�but en minutes
3. Entrez le temps de fin en minutes
4. Choisissez l'emplacement de sauvegarde avec le bouton "????"
5. Cliquez sur "?????" pour d�marrer le t�l�chargement

## Code Source