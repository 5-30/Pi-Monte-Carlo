from random import uniform

# On crée les variables pour compter les points dans le cercle et le nombre total de points placés.
points = 0
pointsDedans = 0

while points < 100000000:
    pointAleatoire = (uniform(-1.0, 1.0), uniform(-1.0, 1.0)) # on prend deux nombre aléatoires entre -1 et 1 pour représenter des coordonnées dans un carré 2x2.
    points += 1

    if (pointAleatoire[0]**2 + pointAleatoire[1]**2) <= 1: # On vérifie que la distance entre le centre du repère et le point est inférieure à 1 (= rayon du cercle)
        pointsDedans += 1

    probaPointDedans = pointsDedans/points
    # probaPointDedans = Acercle/Acarré, donc probaPointDedans = pi*r**2/4*r**2, donc en simplifiant probaPointDedans = pi/4, et donc pi = 4*probaPointDedans

pi = 4*probaPointDedans

print(f"la valeur approchée de pi est {pi}")