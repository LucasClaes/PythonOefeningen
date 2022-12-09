Getal = float(input("Geef een getal waarvan je het eerste cijfer na de komma wilt weten: "))
Rest = (Getal - (Getal // 1)) + 0.00001
Oplossing = int((Rest * 10) // 1)
print(Oplossing)