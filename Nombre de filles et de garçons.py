fille = 50
garçon = 0
Total = fille + garçon


if fille >= 0 and garçon >= 0:
  print(f"Le nombre total d'élèves est de {Total}")

if fille < 0:
    print("Veuillez entrer un nombre de filles valide")
if garçon < 0:
    print("Veuillez entrer un nombre de garçons valide")
elif fille > garçon:
    print("Il y a plus de filles que de garçons")
elif garçon > fille:
    print("Il y a plus de garçons que de filles")
else:
    print("Il y a autant de filles que de garçons")

if fille == 0:
    print("Il n'y a pas de filles")
if garçon == 0:
    print("Il n'y a pas de garçons")


