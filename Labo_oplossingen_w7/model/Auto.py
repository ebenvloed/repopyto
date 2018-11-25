class Auto:
    def __init__(self, par_kleur, par_merk, par_brandstof, par_model, par_kmstand=0):
        self.kleur = par_kleur
        self.__merk = par_merk      # merk heeft geen setter dus rechtsstreeks wegschrijven naar attr.
        self.__brandstof = par_brandstof        # brandstof heeft geen setter dus rechtsstreeks wegschrijven naar attr.
        self.__model = par_model        # brandstof heeft geen setter dus rechtsstreeks wegschrijven naar attr.
        self.kmstand = par_kmstand

    @property
    def kleur(self):
        return self.__kleur

    @kleur.setter
    def kleur(self, value):
        self.__kleur = value

    @property
    def merk(self):
        return self.__merk

    #MERK MAG ENKEL WORDEN OPGEVRAAGD NIET INGESTELD
    # @merk.setter
    # def merk(self, value):
    #     self.__merk = value

    @property
    def brandstof(self):
        return self.__brandstof

    # @brandstof.setter
    # def brandstof(self, value):
    #     self.__brandstof = value

    @property
    def model(self):
        return self.__model

    # @model.setter
    # def model(self, value):
    #     self.__model = value

    @property
    def kmstand(self):
        return self.__kmstand

    @kmstand.setter
    def kmstand(self, value):
        self.__kmstand = value

    def __str__(self):
        return "Auto ------ kleur: {0} --- merk: {1} --- brandstof: {2} --- model: {3} --- kmstand: {4}"\
            .format(self.kleur, self.merk, self.brandstof, self.model, self.kmstand)

    def rijden(self, extra_km):
        self.kmstand = self.kmstand + extra_km              # => self.kmstand += extra_km
