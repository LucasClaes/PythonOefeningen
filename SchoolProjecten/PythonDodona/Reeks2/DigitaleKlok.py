Invoer = int(input("Geef je tijd in minuten: "))
Uren = (Invoer // 60) - (((Invoer // 60)//24) * 24)
Minuten = int((((Invoer / 60) % 1) * 60) // 1)
print(f"{Uren} {Minuten}")