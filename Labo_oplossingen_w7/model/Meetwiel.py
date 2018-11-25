import math


class Meetwiel:
    def __init__(self, par_straal, par_omwentelingen=0):    # , par_omtrek, par_afstand
        self.straal = par_straal
        self.omwentelingen = par_omwentelingen

    @property
    def straal(self):
        return self.__straal

    @straal.setter
    def straal(self, value):
        # controleer of value groter is dan 0 en een kommagetal
        # erste groter dan controleren ging niet want het was een string
        # als je eerst de instance controleerd dan ben je zeker dat het een foat was
        # bije een and zal de tweede voorwaarde niet uitgevoor als de eerste false was
        if (isinstance(value, float) or isinstance(value, int)) and value > 0:
            self.__straal = value
        else:
            self.__straal = 0

    @property
    def omwentelingen(self):
        return self.__omwentelingen

    @omwentelingen.setter
    def omwentelingen(self, value):
        if (isinstance(value, float) or isinstance(value, int)) and value >= 0:
            self.__omwentelingen = value
        else:
            self.__omwentelingen = 0

    @property
    def omtrek(self):
        return math.pi * 2 * self.straal

    @property
    def afstand(self):
        return self.omwentelingen * self.omtrek

    def __str__(self):
        return "Als de straal {0} is en het aantal omwentelingen {1}, dan is de omtrek {2} en de afstand {3}"\
            .format(self.straal, self.omwentelingen, round(self.omtrek, 2), round(self.afstand, 2))
