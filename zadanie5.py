import random
punkty = []
for i in range(15):
    punkty.append(round(random.uniform(0,50) , 2))
print("Wartość listy punkty: " , punkty)
print("Najmniejsza wartość: " , min(punkty))
print("Największa wartość: " , max(punkty))

liczba = float(input("Podaj szukaną liczbę: "))
punkty.index(liczba)
if liczba in punkty:
    print(punkty.index(liczba))
else:
    print("Nie ma takiej liczby")
suma = sum(punkty)
srednia  = round(suma/len(punkty) , 2)
print("Średnia ilość punktów wynosi: " , srednia )
powyzej = []
ponizej = []
for i in punkty:
    if i<srednia:
        ponizej.append(i)

powyzej=[i for i in punkty if i > srednia]
print("Punkty powyzej sredniej: " , powyzej)
print("Punkty ponizej sredniej: " , ponizej)