import random


# Fonction pour déplacer un point dans le tableau en évitant les bords
def deplacer_point(position, direction):
    x, y = position

    # Vérifier si le déplacement est autorisé
    if (
        (direction == "haut" and x > 0)
        or (direction == "bas" and x < 3)
        or (direction == "gauche" and y > 0)
        or (direction == "droite" and y < 3)
    ):
        # Déplacer le point
        if direction == "haut":
            x -= 1
        elif direction == "bas":
            x += 1
        elif direction == "gauche":
            y -= 1
        elif direction == "droite":
            y += 1

    return x, y

# Exemple d'utilisation
position_initiale = (2, 2)
nouvelle_position = deplacer_point(position_initiale, "droite")

# Afficher le tableau avec le point déplacé
tableau[nouvelle_position] = 2
print(tableau)

#Gerer les limites du tableau(faut pas que les elements depassent la limite)
#Gerer la position des elements du tableau(la position doit etre  aléatoire et doit etre compris entre (1,1) et  (4,4))
#Gérer les collision entre éléments ( si on a le meme chiffres cote a cote on fusionne, sinon il restent à côté)
#Gérer la situation ou il est impossibles d'ajouter les elements du tableau (vérifier l'impossibilité de fusionner les cases du tableau, /
# /verifier que l'espace alloué soit bel et bien occupé dans sa totalité)