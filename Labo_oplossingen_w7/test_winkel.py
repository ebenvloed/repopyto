from model.Winkelkar import Winkelkar

ikeakarretje = Winkelkar()


# return alle producten uit de kar
print(ikeakarretje.producten)
# voeg producten, toe via een funtie
ikeakarretje.voeg_product_toe("  malm")
ikeakarretje.voeg_product_toe("  matras")
ikeakarretje.voeg_product_toe("  kast")
ikeakarretje.voeg_product_toe("  bed")
#print(ikeakarretje)
ikeakarretje.verwijder_product("  kast")
print(ikeakarretje)

tweedewinkelkar = Winkelkar()
tweedewinkelkar.voeg_product_toe("  boek")
tweedewinkelkar.voeg_product_toe("  knuffel")
tweedewinkelkar.voeg_product_toe("  boot")
tweedewinkelkar.voeg_product_toe("  kinderkamer")
print(tweedewinkelkar)

winkelkartotaal = ikeakarretje + tweedewinkelkar
print(winkelkartotaal)
