# mark directory as sources root
from model.Boek import Boek
b = Boek("Python for dummies", "StijnW", "Howest", "007", 2019)
b.title = "Python voor gevorderden"
b.title = "Python voor gemiddelde"
boektitel = "Anja en de zeven dwergen"
b.title = boektitel
tweedetitel = b.title + " deel II"
print(tweedetitel)
print(b.jaargang)
print(b)
