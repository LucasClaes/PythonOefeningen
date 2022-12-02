Getal = input("Geef een willekeurig getal waarvan je het tiental en de eenheid wilt omwisselen: ")
Getal = "00" + Getal
x = Getal[-1]
y = Getal[-2]
z = int(Getal[-2:])
print(f"{x} , {y} , {z}")
oplossing = (int(Getal) - z) + (int(x) *10) + int(y)
print(oplossing)

