import random
class Geboortedatum:
    __aantal_data = 0

    def __init__(self, par_dag, par_maand, par_jaar):
        self.maand = par_maand
        self.dag = par_dag
        self.jaar = par_jaar
        Geboortedatum.__aantal_data += 1

    @property
    def dag(self):
        return self.__dag

    @dag.setter
    def dag(self, value):
        if isinstance(value, int) and self.__controle_dag(value):
            self.__dag = value
        else:
            self.__dag = -1

    @property
    def maand(self):
        return self.__maand

    @maand.setter
    def maand(self, value):
        if isinstance(value, int) and value in range(1, 13):
            self.__maand = value
        else:
            self.__maand = -1

    @property
    def jaar(self):
        return self.__jaar

    @jaar.setter
    def jaar(self, value):
        if isinstance(value, int):
            self.__jaar = value
        else:
            self.__jaar = -1

    # hulp methode
    # deze zetten we private zodat die niet buiten de klasse kan gebruikt worden
    def __controle_dag(self, value):
        if self.__maand in [1, 3, 5, 7, 8, 10, 12]:
            if value > 0 and value <= 31:
                return True
        elif self.__maand in [4, 6, 9, 11]:
            if value > 0 and value <= 30:
                return True
        else:
            # nu is het zeker february
            if value > 0 and value <= 29:
                return True
        # als hij nooit return heeft gehad is dit geen geldige datum
        return False

    @staticmethod
    def genereer_willerkeurig():
        jaar = random.randint(1900, 2018)
        maand = random.randint(1, 12)
        dag = random.randint(1, 31)

        res = Geboortedatum(dag, maand, jaar)
        return res


    def __str__(self):
        return "Geboortedatum : {0}/{1}/{2}".format(self.dag, self.maand, self.jaar)

""""
    def __str__(self):
        return "Geboortedatum : {0}".format(self.res)
"""