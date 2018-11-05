#!/usr/bin/env python3
# nom : 1a-add.py
# auteur : lucas erisset
# date : 15/10/18
# fonction qui calcule 2 nombres entre eux


def add(nb1, nb2):
        return print(nb1+nb2)

# l'utilisateur entre 2 nombres
int1 = input('premier chiffre : ')
int2 = input('deuxieme chiffre : ')

# on test si ce sont des entiers sinon on rencoi une erreur
try:
        int1 = int(int1)
        int2 = int(int2)
except ValueError:
        print("ce n'est pas un chiffre")
        exit()

add(int1, int2)