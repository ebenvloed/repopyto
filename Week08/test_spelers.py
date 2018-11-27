from model.ploeg.Spelers import Spelers

sp1 = Spelers("VanDerWalen", "Stijn", 5)
sp2 = Spelers("Nano", "Lissa", 10)

sp2.score = 11
print(Spelers.teamscore())


