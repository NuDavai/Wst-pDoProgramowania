import random

zestaw_1 = []
x = int(input("Podaj liczbe elementow pierwszej listy: "))
for i in range(x):
    zestaw_1.append(random.randint(1,10))
    print(zestaw_1[i])

zestaw_2 = []
y = int(input("Podaj liczbe elementow drugiej listy: "))
for i in range(y):
    zestaw_2.append(random.randint(1,10))
    print(zestaw_2[i])

y = int(input("Podaj szukana liczbe: "))
#...
