Datum = int(input("Geef een datum: "))
Weekdag = Datum - Datum // 7 * 7 

if (Weekdag + 3) > 6 :
  print((Weekdag + 3) - 7)
else :
  print(Weekdag + 3)