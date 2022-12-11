Geheel = int(input("Geef de gehele prijs van 1 koekje: "))
Decimaal = float(input("Geef de decimale prijs van 1 koekje: "))
Koekjes = int(input("Hoeveel koekjes wil je kopen?: "))

PrijsKoekje = Geheel + (Decimaal / 100)
Prijs = (PrijsKoekje * Koekjes) + 0.001

GehelePrijs = Prijs // 1
DecimalePrijs = ((Prijs - (Prijs // 1)) * 100) // 1

print(f"{int(GehelePrijs)} {int(DecimalePrijs)}")