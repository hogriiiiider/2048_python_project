import random
import create_grid as np

# Création d'un tableau 4x4 rempli de zéros
tableau = np.zeros((4, 4), dtype=int)

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