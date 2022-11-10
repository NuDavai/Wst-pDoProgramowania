import random

n = int(input("Podaj liczbe elementow pierwszej listy: "))
zestaw_1 = []
for i in range(n):
    zestaw_1.append(random.randint(1,10))
print(zestaw_1)

n = int(input("Podaj liczbe elementow drugiej listy: "))
zestaw_2 = [random.randint(5,15) for i in range(n)]
print(zestaw_2)

x = int(input("Podaj szukaną liczbę: "))
if x in zestaw_1:
    print("Liczba znajduje się w zestawie pierwszym")
if x in zestaw_2:
    print("Liczba znajduje się w zestawie drugim")
else:
    print("Liczba nie znajduje się w żadnym z powyższych zestawów")

zestaw_1_2 = zestaw_1 + zestaw_2
zestaw_1_2.sort()
print(zestaw_1_2)