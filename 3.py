#Napisz skrypt działający jak prosty kalkulator, który potrafi dodawać, odejmować, mnożyć,
#dzielić oraz obliczać potęgę.

#print("")
#x = input("Podaj argument 1: ")
#y = input("Podaj agrument 2: ")
#print("Wynik: ")

print("Jaki numer operacji chcesz wykonać?")
print("1 Dodawanie")
print("2 Odejmowanie")
print("3 Dzielenie")
print("4 Mnożenie")
print("5 Potęgowanie")
a = input("numer: ")
x = input("Podaj argument 1: ")
y = input("Podaj agrument 2: ")
if a==1:
    z = x+y
elif a==2:
    z = x-y
elif a==3:
    z = x/y
elif a==4:
    z = x * y
elif a==5:
    z = x**y
print("Wynik: ", z )
