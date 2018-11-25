from model.Auto import Auto
import random

garage = []
auto1 = Auto("rood", "Tesla", "elektrisch", "Model S", 0)
auto2 = Auto("groen", "VW", "diesel", "Polo", 0)
garage.append(auto1)
garage.append(auto2)

# je kan ook een object aanmaken via de invoer van de gebruiker
kl = input("geef een kleur: ")
merk = input("geef een merk: ")
km_stand = int(input("geef een km stand: "))

auto3 = Auto(kl, merk, "diesel", "golf", km_stand)
garage.append(auto3)

auto2.rijden(50)
auto2.rijden(70)
# print("{0} heeft zoveel km op de teller: {1}".format(auto2.merk, auto2.kmstand))
print(garage)

# er zitten 3 items in mijn lijst
# overlopen en elke auto laten rijden.
print("op het einde van de dag")
for element in garage:
    element.rijden(random.randint(0, 100))

for element in garage:
    print(element)
