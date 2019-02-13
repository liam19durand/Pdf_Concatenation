"""Implémenté par William DURAND
pdf_concat: Ce script permet de parcourir tous les dossiers présents dans le dossier courant, 
et de concaténer les pdf.
Attention ! Il est nécessaire d'installer PyPDF2 !"""

import os
import sys
from PyPDF2 import PdfFileMerger

try:
    argument = sys.argv[1]
    for dir in os.listdir(argument):
        #Création d'une variable stockant le chemin absolu (avec nom du dossier)
        path = argument + '\\' + dir
        if os.path.isdir(path):
            #Permet de récupérer tous les pdf du dossier courant et de les stocker dans une liste
            pdfs = [a for a in os.listdir(path) if a.endswith(".pdf") or a.endswith(".PDF")] 
            merger = PdfFileMerger()
            for pdf in pdfs:
                #Création d'une variable stockant le chemin absolu (avec nom du pdf)
                pathPdf = path + '\\' + pdf
                merger.append(open(pathPdf, 'rb'))

            #Création d'une variable correspondant au nom du pdf produit
            nameFile = argument + "\\" + dir + ".pdf"

            with open(nameFile, "wb") as fout:
                merger.write(fout)
except:
    print("Aucun argument / argument non disponible")
