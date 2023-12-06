class c2048:

    def __init__(self, dim=4):
        self.jeu = self.creer_jeu(dim)
        self.coup = 0
        self.score = 0

    def creer_jeu(self, dim):
        return creer_jeu(dim)

    def __repr__(self):
        return "coup=%d score=%d, jeu=\n%s" % (self.coup, self.score, self.jeu)

    def position_libre(self):
        pos = []
        for i in range(self.jeu.shape[0]):
            for j in range(self.jeu.shape[1]):
                if self.jeu[i, j] == 0:
                    pos.append((i, j))
        return pos

    def calcule_score(self):
        return self.jeu.max()

    def joue_ligne_colonne(self, lc):
        # on enlève les 0
        non_null = [a for a in lc if a != 0]
        # on additionne les nombres identiques consécutifs
        i = len(non_null) - 1
        while i > 0:
            if non_null[i] != 0 and non_null[i] == non_null[i-1]:
                non_null[i-1] *= 2
                non_null[i] = 0
                i -= 2
            else:
                i -= 1
        # on enlève à nouveau les zéros
        non_null2 = [a for a in non_null if a != 0]
        final = numpy.zeros(len(lc), dtype=int)
        final[:len(non_null2)] = non_null2
        return final

    def joue_coup(self, direction):
        if direction == 0:  # gauche
            for i in range(self.jeu.shape[0]):
                self.jeu[i, :] = joue_ligne_colonne(self.jeu[i, :])
        elif direction == 1:  # droite
            for i in range(self.jeu.shape[0]):
                self.jeu[i, ::-1] = joue_ligne_colonne(self.jeu[i, ::-1])
                # identique à
                # self.jeu[i, :] = joue_ligne_colonne(self.jeu[i, ::-1])[::-1]
        elif direction == 2:  # haut
            for i in range(self.jeu.shape[0]):
                self.jeu[:, i] = joue_ligne_colonne(self.jeu[:, i])
        elif direction == 3:  # bas
            for i in range(self.jeu.shape[0]):
                self.jeu[::-1, i] = joue_ligne_colonne(self.jeu[::-1, i])

    def nombre_aleatoire(self):
        pos = self.position_libre()
        nb = numpy.random.randint(0, 2) * 2 + 2
        i = numpy.random.randint(0, len(pos))
        p = pos[i]
        self.jeu[p] = nb

    def perdu(self):
        pos = self.position_libre()
        return len(pos) == 0

    def coup_suivant(self):
        # une direction aléatoire parmi 0 ou 4
        h = numpy.random.randint(0, 2)
        return h * 2

    def partie(self):
        self.coup = 0
        while not self.perdu():
            self.nombre_aleatoire()
            d = self.coup_suivant()
            self.joue_coup(d)
            self.coup += 1
        self.score = self.calcule_score()

J = c2048()
J.partie()
J