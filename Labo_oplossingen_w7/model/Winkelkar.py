class Winkelkar:
    def __init__(self):
        # de init heeft geen parameters
        self.producten = []
        #maar wordt wel een lege list aangemaakt

    # @property
    # def producten(self):
    #     print("winkelkar getter")
    #     return self.__producten

    # @producten.setter
    # def producten(self, value):
    #     print("winkelkar setter" + value)
    #     self.__producten = value


    def voeg_product_toe(self, nieuw_product):
        print("winkelkar voeg_product_toe" + nieuw_product)
        self.producten.append(nieuw_product)
        return


    def verwijder_product(self, product):
        print("winkelkar verwijder_product" + product)
        # vraag: hoe kan ik de fout negeren als het product niet bestaat.
        self.producten.remove(product)
        return

    def __add__(self, tweedewinkelkar):
#        print("add winkelkar met producten" + tweedewinkelkar)
        nieuwe_winkelkar = Winkelkar()
        winkelkartotaal = self.producten + tweedewinkelkar.producten
        
        return nieuwe_winkelkar


    def __str__(self):
        return "Winkelkar : {0}".format(self.producten)



# +     object.__add__(self, other)
# +=        object.__iadd__(self, other)