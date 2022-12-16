
getal = input("Geef een getal waarvan je wilt weten of het stijgend is: ")

getal1 = int(getal[-3])
getal2 = int(getal[-2])
getal3 = int(getal[-1])

if (getal3 - getal2) >= 1 and (getal2 - getal1) >= 1: print("STIJGEND")
else: print("NIET (!) STIJGEND")
