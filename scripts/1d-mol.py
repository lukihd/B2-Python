#!/usr/bin/env python3
# nom : 1d-mol.py
# auteur : lucas Erisset
# date : 23/10/18
# jeux du plus ou moins en Python

import re
import random
import signal

# fonctions
def restart ():
    restartValue = input("Voulez vous rejouer oui(o)/non(n) : ")
    if restartValue is "o" or restartValue is "O":
        return True
    elif restartValue is "n" or restartValue is "N":
        return False
    else:
        return print("Va te payer un café au lieu de tout casser") 

# on verifie avec la regex si la valeur est un entier 
def checkType (valueToCheck):
    if re.match('^[0-9]+$', valueToCheck):
        valueToCheck = int(valueToCheck)
        if valueToCheck > 100:
            return False
        else:
            return True
    else:
        return False

# quiter proprement
def checkExit (valueToCheck):
    if valueToCheck == "q" or valueToCheck == "Q":
        print ("Au revoir, la solution était : " + str(intToFind))
        return exit()

# interception des signaux (ctrl-c)
def checkSignal(sig, frame):
        print ("Au revoir, la solution était : " + str(intToFind))
        return exit()

signal.signal(signal.SIGINT, checkSignal)
signal.signal(signal.SIGTERM, checkSignal)

# le jeu
restartGame = True

while restartGame == True:
    intToFind = random.randint(0, 100)

    inputUsr = input("Entrez un chiffre entre 0 et 100 : ")
    checkExit(inputUsr)

    while inputUsr != intToFind:

        while checkType(inputUsr) == False:
            inputUsr = input("Vous devez entrer un chiffre entre 0 et 100 (pas des lettres ou autres) : ")
            checkExit(inputUsr)
    
        inputUsr = int(inputUsr)
        if inputUsr > intToFind:
            inputUsr = input("Moins : ")
        elif inputUsr < intToFind:
            inputUsr = input("Plus : ")
        
    print("Vous avez gagné !")
    restartGame = restart()