from model.Meetwiel import Meetwiel


fietswiel = Meetwiel(2)
autowiel = Meetwiel(0.5, 2)
karrewiel = Meetwiel("2", -4)

print(fietswiel)
print(autowiel)
print(karrewiel)


print("*********************")
wiel = Meetwiel(0.9, 5)
print(wiel)

invoer = input("geef het aantal extra omwentelingen op: ")
while invoer != "c":
    wiel.omwentelingen += int(invoer)
    invoer = input("geef het aantal extra omwentelingen op: ")

print(wiel)
print("Meetwiel legde reeds {0} km af".format(round(wiel.afstand, 2)))
