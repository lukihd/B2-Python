#!/usr/bin/env python3
# nom : 1b-dic.py
# auteur : lucas erisset
# date : 15/10/18
# script qui affiche les noms rentrés par l'utilisateurs dans l'ordre alphabéthique


def dicoName():
        list_name = []
        i = 0
        exitProgram = False

        # Boucle qui permet d'itéré les entrée utilisateurs dans la base puis qui tri par ordre alphabéthique
        while exitProgram == False:
                i += 1
                user_input = input("le nom à insérer dans le dictionnaire : ")
                if user_input == "q" or user_input == "Q":
                        exitProgram = True
                        break
                list_name.append(user_input)
        list_trie = sorted(list_name)
        return print(list_trie)


dicoName()