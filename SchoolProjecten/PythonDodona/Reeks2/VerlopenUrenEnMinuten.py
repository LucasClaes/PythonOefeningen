Tijd = int(input("Geef het aantal seconden die verlopen zijn: "))
Uur = (Tijd / 3600)
Uren = (Uur // 1)
Minuten = (Uur % 1 * 60) // 1
Seconden = Tijd - (Uren * 3600 + Minuten * 60)
print(f"{int(Uren - ((Uren // 24) * 24))}:{int(Minuten)}:{int(Seconden)}")