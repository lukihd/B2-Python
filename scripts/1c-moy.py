#!/usr/bin/env python3
# nom : 1c-moy.py
# auteur : lucas erisset
# date : 15/10/18
# script affichant la moyenne des notes et prénoms des personnes et un top 5 des notes

# fonction top5 mais je n'arrive pas à la faire
#def Top5 (valueDict):
#  i = 0
#  concatVal = ""
#  valueDict = sorted(valueDict)
#  for name,score in valueDict.items():
#    if i < 5:
#      print(name + " " + score)
#    i += 1
#  return concatVal

# le script de la moyenne :
dict_score = {}
i = 0
exitWhile = False

while exitWhile == False:
  i+= 1
  name_input = input("le nom à insérer dans le dictionnaire : ")
  if name_input == "q":
    exitWhile = True
  else:
    score_input = input("la note de l'élève : ")
    try:
      score_input = int(score_input)
      if score_input > 20 or score_input < 0:
        print("la note doit être entre 0 et 20")
        exit()
    except ValueError:
      print("ce n'est pas un chiffre")
      exit()
  dict_score[name_input] = score_input

score_total = 0
for name in dict_score:
  score_total += dict_score[name]

quotient = len(dict_score)
moyenne = score_total/quotient
moyenne =  str(moyenne)
print("la moyenne est de "+moyenne)

Top5(dict_score)