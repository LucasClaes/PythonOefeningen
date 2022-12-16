
# x en y positie van je eerste veld krijgen
x1 = int(input("Geef de x positie van je eerste veld:"))
y1 = int(input("Geef de y positie van je eerste veld:"))

# x en y positie van je tweede veld krijgen
x2 = int(input("Geef de x positie van je tweede veld:"))
y2 = int(input("Geef de y positie van je tweede veld:"))


#Iets dat we nog niet geleerd hebben maar het spaart me veel moeite
def kleur(x_positie,y_positie):

    #Kijken of dat getal x even of oneven is
    x1 = x_positie // 2
    x2 = x_positie / 2

    if x1 < x2: x = "oneven"
    else: x = "even"

    #Kijken of dat getal y even of oneven is
    y1 = y_positie // 2
    y2 = y_positie / 2

    if y1 < y2: y = "oneven"
    else: y = "even"

    #Kijken ofdat het een licht of donker veld is
    if x == "even" and y == "oneven": antwoord = "LICHT VELD"
    elif x == "oneven" and y == "even": antwoord = "LICHT VELD"
    else: antwoord = "DONKER VELD"

    #Variable antwoord terug geven
    return(antwoord)



#Variable antwoord die we terugkrijgen uit onze functie gebruiken om te kijken ofdat de twee velden dezelfde kleur hebben
if kleur(x1,y1) == kleur(x2,y2): print("Zelfde Kleur")
else: print("Niet zelfde kleur")
