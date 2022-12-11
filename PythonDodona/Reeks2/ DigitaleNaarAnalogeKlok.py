Tijd1 = int(input("Wat is het uurtal van de digitale tijd: "))
Tijd2 = int(input("Wat is het uurtal van de digitale tijd:"))
Aftrekking = (Tijd1//12) * 12
Oplossing = ((Tijd1- Aftrekking)*30) + (Tijd2 / 2)
print(int(Oplossing))