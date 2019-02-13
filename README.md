# Introduction
Ce projet contient un script Python permettant de parcourir tous les sous-dossiers présents dans un dossier, et de concaténer les pdf. 

L'exécution du script nécessite le passage en argument du **chemin absolu** indiquant l'emplacement du dossier en question.

<u>Exemple</u> :

```powershell
python pdf_concat.py C:\MonDossier
```

Les pdf ainsi obtenu seront alors disponibles dans le dossier indiqué par le chemin absolu. 

# Prérequis
Afin que le script fonctionne, il est nécessaire d'avoir installer **Python 3.7**, ainsi que le package Python **PyPDF2**.

## Installation de PyPDF2
L'utilisation de **pip** est conseillé dans le cadre de l'installation de module. Assurez-vous donc que **pip** soit installé sur votre machine, puis utiliser la commande suivante : `python -m pip install PyPDF2`


Une fois **PyPDF2** installé, vous pourrez profiter des fonctionnalités du script.
    
