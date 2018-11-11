#!/usr/bin/env python3
# nom : 2a-mol.py
# auteur : lucas Erisset
# date : 04/11/18
# jeux du plus ou moins en Python qui inscrit dans un document cible ( ne fonctionne pas à cause des droits sur mol.txt que je n'arrive pas a rendre 'write' )

import re
import random
import signal
from time import sleep

# regex pour vérifier un int
def checkType(valueToCheck):
    if re.match('^[0-9]+$', valueToCheck):
        valueToCheck = int(valueToCheck)
        if valueToCheck > 100:
            return False
        else:
            return True
    else:
        return False

# verification de la sortie du script
def checkExit(valueToCheck):
    if valueToCheck == "q" or valueToCheck == "Q":
        WriteIn("Au revoir, la solution était : " + str(intToFind))
        return exit()

# ecris dans le document cible la valeur en parametre
def WriteIn(valueToSend):
    fileTxt = open("mol.txt", "w")
    fileTxt.write(valueToSend)
    fileTxt.close()

# lis le document cible
def ReadIn():
    fileTxt = open("mol.txt", "r")
    valueToRead = fileTxt.read()
    fileTxt.close()
    return valueToRead

# signaux d'arret du script
def checkSignal(sig, frame):
    print("Au revoir, la solution était : " + str(intToFind))
    return exit()


signal.signal(signal.SIGINT, checkSignal)
signal.signal(signal.SIGTERM, checkSignal)

# le jeu
intToFind = random.randint(0, 100)
print(intToFind)

stop = False

WriteIn("bienvenu")

while stop is False:
    sleep(1)    
    usrValue = ReadIn()
    checkExit(usrValue)

    if checkType(usrValue) is False:
            print("not a number")
            continue
    else:
        usrValue = int(usrValue)

        if usrValue < intToFind:
                WriteIn("plus")
        elif usrValue > intToFind:
                WriteIn("moins")
        else:
                stop = True    

WriteIn("Vous avez gagne !")
