Positie = int(input("Geef de positie van de kleoine wijzer in graden"))

Aftrekking = (Positie // 30) * 30
Oplossing = (Positie - Aftrekking) * 12

print(Oplossing)