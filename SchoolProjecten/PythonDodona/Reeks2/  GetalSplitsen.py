Getal = int(input("Geef een getal dat je wilt splitsen: "))
Getal2 = Getal % 10
Getal1 = int((Getal - Getal2) / 10)
print(f"{Getal1} {Getal2}")