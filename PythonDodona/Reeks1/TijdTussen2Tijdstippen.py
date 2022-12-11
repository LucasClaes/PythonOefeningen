
T1_U1 = input("Geef het urental van je eerste uur: ")
T2_U1 = input("Geef het aantal minuten van je eerste uur: ")
T3_U1 = input("Geef het aantal seconden van je eerste uur: ")

T1_U2 = input("Geef het urental van je tweede uur: ")
T2_U2 = input("Geef het aantal minuten van je tweede uur: ")
T3_U2 = input("Geef het aantal seconden van je tweede uur: ")

T1 = (int(T1_U1) * 3600) + (int(T2_U1) * 60) + int(T3_U1)
T2 = (int(T1_U2) * 3600) + (int(T2_U2) * 60) + int(T3_U2)

oplossing = int(T2) - int(T1)

print(int(oplossing))