Lista = []
print("Podaj 6 liczb ")
for i in range(6):
    x = int(input("Podaj liczbe: "))
    if (x%2!=0):
        if (x>20):
            Lista.append(x)
print(Lista)