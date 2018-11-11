#!/usr/bin/env python3
# nom : 2b-auto.py
# auteur : lucas Erisset
# date : 10/11/18
# Script qui interargi avec 2a-mol.py et le resou. (il faut lancer 2a-mol.py avant puis ca se debrouille tout seul)

from random import randint
from time import sleep

# ecris dans le document cible la valeur en parametre
def WriteIn(valueToSend):
    fileTxt = open("2a-mol/mol.txt", "w")
    fileTxt.write(valueToSend)
    fileTxt.close()

# lis le document cible
def ReadIn():
    fileTxt = open("2a-mol/mol.txt", "r")
    valueToRead = fileTxt.read()
    fileTxt.close()
    return valueToRead

# defini la valeur a rentrer dans le document
def ValueToReturn(valueFile, valueTest, valueMax, valueMin):
    print(valueFile)
    if valueFile == "moins":
        testMax = valueTest
    elif valueFile == "plus":
        testMin = valueTest
    valueTest = round((valueMax + valueMin)/2)
    return valueTest

solution = "Vous avez gagne !"
valueInFile = ""
testInt = randint(0, 100)
testMax = 100
testMin = 0

while valueInFile != solution:
    print(testInt)
    WriteIn(str(testInt))
    sleep(1)
    valueInFile = ReadIn()
    if valueInFile == "moins":
        testMax = testInt
    elif valueInFile == "plus":
        testMin = testInt
    testInt = round((testMax + testMin)/2)
exit()