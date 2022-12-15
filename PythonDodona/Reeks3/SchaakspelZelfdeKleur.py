

kleur(x_positie = 10, y_positie = 2)




def kleur(x_positie,y_positie):
    x1 = x_positie // 2
    x2 = x_positie / 2
    if x1 < x2:
        x = "oneven"µ
    else:
        x = "even"

    y1 = y_positie // 2
    y2 = y_positie / 2

    if y1 < y2:
        y = "oneven"
    else:
        y = "even"

    if x == "even" and y == "oneven":
        antwoord = "LICHT VELD"
    elif x == "oneven" and y == "even":
        antwoord = "LICHT VELD"
    else:
        antwoord = "DONKER VELD"

    return(antwoord)