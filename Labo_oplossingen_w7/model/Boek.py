class Boek:
    # constructor (init)
    def __init__(self, par_title, par_auteur, par_uitgever, par_isbn, par_jaargang):
        self.title = par_title
        self.auteur = par_auteur
        self.uitgeverij = par_uitgever
        self.isbn = par_isbn
        self.jaargang = par_jaargang
        # hier gebruik je al de SET propperties van de klasse

    # properties (getters/setters)
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value    # de waarde die binnenkomt zal worden opgeslagen in het attribuut __title

    @property
    def auteur(self):
        return self.__auteur

    @auteur.setter
    def auteur(self, value):
        self.__auteur = value

    @property
    def uitgeverij(self):
        return self.__uitgeverij.upper()

    @uitgeverij.setter
    def uitgeverij(self, value):
        self.__uitgeverij = value

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        self.__isbn = value

    @property
    def jaargang(self):
        return self.__jaargang

    @jaargang.setter
    def jaargang(self, value):
        # hier controlleer je of dat de jaarhgangen binnen normale waarden liggen
        # dan sla je op of verander je het naar 2000
        if value > 1900 and value < 2018:
            self.__jaargang = value
        else:
            self.__jaargang = 2000

    # string functie vanonder in file
    def __str__(self):
        return "Boek : {0} - {1} : {2}".format(self.title, self.auteur, self.uitgeverij)
