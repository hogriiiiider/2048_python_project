import random

# Fonction pour générer un nombre avec les probabilités spécifiées
def generer_nombre():
    rand_num = random.randint(1, 10)
    if rand_num <= 9:
        return 2
    else:
        return 4

# Exemple d'utilisation
nombre_genere = generer_nombre()
print(nombre_genere)
