Getal = input("Geef een getal dat kleiner dan 1000 is: ")
Getal = "00" + Getal
x = int(Getal[-3])
y = int(Getal[-2])
z = int(Getal[-1])
#print(f"{x} , {y} , {z}")
print(x + y + z)