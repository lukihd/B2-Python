#!/usr/bin/env python3
# nom : 2a-mol.py
# auteur : lucas Erisset
# date : 04/11/18
# jeux du plus ou moins en Python qui inscrit dans un document cible ( ne fonctionne pas à cause des droits sur mol.txt que je n'arrive pas a rendre 'write' )

import re
import random
import signal

# recommencer le jeu a la fin de la partie
def restart():
    WriteIn("Voulez vous rejouer oui(o)/non(n) : ")
    restartValue = ReadIn()
    if restartValue is "o" or restartValue is "O":
        return True
    elif restartValue is "n" or restartValue is "N":
        return False
    else:
        return WriteIn("Va te payer un café au lieu de tout casser")

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
        print("Au revoir, la solution était : " + str(intToFind))
        return exit()

# ecris dans le document cible la valeur en parametre
def WriteIn(valueToSend):
    fileTxt = open("mol.txt", "w")
    print(valueToSend, fileTxt)
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

restartGame = True

# le jeu
while restartGame == True:
    intToFind = random.randint(0, 100)
    print(intToFind)

    WriteIn("Vous allez commencer à jouer au 'plus ou moins', bonne chance ! Entrez un chiffre entre 0 et 100 : ")
    usrValue = ReadIn()
    checkExit(usrValue)

    while usrValue != intToFind:

        while checkType(usrValue) == False:
            WriteIn("Vous devez entrer un chiffre entre 0 et 100 (pas des lettres ou autres) : ")
            usrValue = ReadIn()
            checkExit(usrValue)

            if usrValue > intToFind:
                WriteIn("moins")
                ReadIn()
            elif usrValue < intToFind:
                WriteIn("plus")
                ReadIn()

    print("Vous avez gagné !")
    restartGame = restart()
