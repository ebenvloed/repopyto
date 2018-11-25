class Bier:
    # consturtor (init)
    def __init__(self, par_naam, par_brouwerij, par_kleur, par_alcohol):
        self.naam = par_naam
        self.brouwerij = par_brouwerij
        self.kleur = par_kleur
        self.alcohol = par_alcohol
    # properties (controle op leeg en perc)

    # to string(__str__)

    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        if value != "":
            self.__naam = value
        else:
            self.__naam = "onbekend"

    @property
    def brouwerij(self):
        return self.__brouwerij

    @brouwerij.setter
    def brouwerij(self, value):
        self.__brouwerij = value

    @property
    def kleur(self):
        return self.__kleur

    @kleur.setter
    def kleur(self, value):
        self.__kleur = value

    @property
    def alcohol(self):
        return self.__alcohol

    @alcohol.setter
    def alcohol(self, value):
        if isinstance(value, float) and value >= 0 and value <= 10:
            self.__alcohol = value
        else:
            self.__alcohol = -1.0

    def __str__(self):
        return "Bier : naam:{0} - brouwerij:{1} - kleur:{2} - alcohol:{3}".format(self.naam, self.brouwerij, self.kleur, self.alcohol)