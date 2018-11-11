import shutil
import os
import gzip
import sys
from time import sleep

def createArchive(archiveName, toArchiveDirectory, dataDirectory):
    shutil.make_archive(archiveName, "gztar")
    shutil.move(archiveName + ".tar.gz", dataDirectory)

toArchiveDirectory = os.path.expanduser("D:/Github/B2-Python")
archiveName = "B2-Pyton"
dataDirectory = os.path.expanduser("~/Data/")

# crée un dossier au chemin en parametre si il n'existe pas
if not os.path.isdir(dataDirectory):
    os.makedirs(dataDirectory)

# on verifie si une archive a deja etait faite
shutil.make_archive(archiveName, "gztar", toArchiveDirectory)

if os.path.exists(dataDirectory + archiveName + ".tar.gz"):
    with gzip.open(dataDirectory + archiveName + ".tar.gz") as file:
        oldArchive = file.read()

    with gzip.open(archiveName + ".tar.gz") as file:
        newArchive = file.read()

    if oldArchive != newArchive:
        os.remove(dataDirectory + archiveName + ".tar.gz")
        createArchive(archiveName, toArchiveDirectory, dataDirectory)
        sys.stdout.write("archive remplacee")

    else:
        sys.stderr.write("archive existe deja")

else:
    createArchive(archiveName, toArchiveDirectory, dataDirectory)
    sys.stdout.write("archive cree")
