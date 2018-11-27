class Spelers:
    # static variabele

    __teamscore = 0

    def __init__(self, par_naam, par_voornaam, par_score):
        self.naam = par_naam
        self.voornaam = par_voornaam
        self.score = par_score
        # verhoog teamscore
        #Spelers.__teamscore += par_score

    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        self.__naam = value

    @property
    def voornaam(self):
        return self.__voornaam

    @voornaam.setter
    def voornaam(self, value):
        self.__voornaam = value

    @property
    def score(self):
        return self.__spelerscore

    @score.setter
    def score(self, value):
        if isinstance(value, int):
            # verhoog teamscore
            if hasattr(self, "score"):
                Spelers.__teamscore -= self.score
            Spelers.__teamscore += value
            self.__spelerscore = value
        else:
            self.__spelerscore = -1

    def __str__(self):
        return "Speler : {0} {1} => {2}".format(self.naam, self.voornaam, self.spelerscore)

    @staticmethod
    # hier gebruik je de naam van de klasse
    def teamscore():
        return Spelers.__teamscore
