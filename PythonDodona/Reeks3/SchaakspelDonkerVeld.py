x_positie = int(input("Geef je x coordinaat: "))
y_positie = int(input("Geef je y coordinaat: "))


x1 = x_positie // 2
x2 = x_positie / 2

if x1 < x2:
    x = "oneven"
else:
    x = "even"

y1 = y_positie // 2
y2 = y_positie / 2

if y1 < y2:
    y = "oneven"
else:
    y = "even"

print(x,y)


if x == "even" and y == "oneven":
    print("LICHT VELD")
if x == "oneven" and y == "even":
    print("LICHT VELD")
else:
    print("DONKER VELD")



