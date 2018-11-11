#!/usr/bin/env python3
# nom : 3b-opt.py
# auteur : lucas Erisset
# date : 11/11/18
# Script en complément du précedent avec de nouvelles possibilités

import shutil
import os
import gzip
import sys
from time import sleep
import signal
import argparse

parser = argparse.ArgumentParser(description="Pour se script inserez : \n 1. le dossier à archiver. \n 2. le nom de l'archive. \n 3. le nom du dossier cible. \n 4. validez par 'y' ou 'n' si vous souhaitez entrer d'autre dossier.")
args = parser.parse_args()

# fonctions

def createArchive(archiveName, toArchiveDirectory, dataDirectory):
    shutil.make_archive(archiveName, "gztar")
    shutil.move(archiveName + ".tar.gz", dataDirectory)

# signaux d'arret du script
def checkSignal(sig, frame):
    sys.stderr.write("Erreur : Archivage interompu")
    return exit()

# fonction qui compare l'espace disponible et celui a louer
def checkSpace(archive, dest):
    sizeArchive = os.path.getsize(archive + ".tar.gz")
    sizeDest = shutil.disk_usage(dest)

    if sizeDest.free > sizeArchive:
        return True
    else:
        return False

signal.signal(signal.SIGINT, checkSignal)
signal.signal(signal.SIGTERM, checkSignal)

# variables
stop = False
endInput = ""

toArchiveDirectory = []
archiveName = []
dataDirectory = []

# on demande a l'utilisateur les archives a faire au demarage du script
while stop == False:  
    goodInput = False

    toArchiveDirectory.append(input("indiquez le.s répertoire.s à compresser :\n"))
    archiveName.append(input("entrez le nom de.s archive.s :\n"))
    dataDirectory.append(input("indiquez le répertoire de destination :\n"))

    while goodInput == False:
        endInput = input("Entrer d'autre répertoire a archiver ? (y / n) :\n")
        
        if endInput is "n":
            goodInput = True
            stop = True
        elif endInput is "y":
            goodInput = True
            continue

# on fais un foreach sur chaque archive a faire (celui ci contient les informations des listes) 
for archDirect, archName, dataDirect in zip(toArchiveDirectory, archiveName, dataDirectory):

    # crée un dossier au chemin en parametre si il n'existe pas
    if not os.path.isdir(dataDirect):
        os.makedirs(dataDirect)

    # on verifie les droits utilisateurs sur la destination
    if os.access(archDirect, os.R_OK and os.W_OK):

        # on verifie les droits utilisateurs sur la destination
        if os.access(dataDirect, os.R_OK and os.W_OK):

            # on verifie si une archive a deja etait faite et on compare les deux
            shutil.make_archive(archName, "gztar", archDirect)
            
            # on vérifie l'espace sur la cible (user/)
            if checkSpace(archName, "d:/"):

                if os.path.exists(dataDirect + archName + ".tar.gz"):
                    with gzip.open(dataDirect + archName + ".tar.gz") as file:
                        oldArchive = file.read()

                    with gzip.open(archName + ".tar.gz") as file:
                        newArchive = file.read()

                    if oldArchive != newArchive:
                        os.remove(dataDirect + archName + ".tar.gz")
                        createArchive(archName, archDirect, dataDirect)
                        sys.stdout.write("Complete : Archive mise a jour \n")

                    else:
                        sys.stderr.write("Erreur : L'archive existe deja \n")
                        exit()
                else:
                    createArchive(archName, archDirect, dataDirect)
                    sys.stdout.write("Complete : L'archive a ete cree \n")

            else:
                sys.stderr.write("Erreur : pas assez de place disponible dans le dossier de destination \n")
                exit()
        else:
            sys.stderr.write("Erreur : vous n'avez pas les droits sur le fichier de destination \n")
            exit()
    else:
        sys.stderr.write("Erreur : vous n'avez pas les droits sur le fichier a archiver \n")
        exit()