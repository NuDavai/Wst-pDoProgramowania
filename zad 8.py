x = int(input("Podaj wysokosc: "))
y = int(input("Podaj szerokosc: "))
znak = str(input("Podaj znak: "))
for i in range(x):
    for j in range(y):
        print(znak, end=' ')
    print("")