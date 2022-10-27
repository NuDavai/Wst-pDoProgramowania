n = int(input("podaj liczbe studentow: "))
i = 1
suma = 0
while i<=n:
    punkty = int(input(f"wprowadz liczbe punktow dla studenta numer {i}: "))
    suma = suma + punkty
    i = i + 1

print("srednia puntkow wynosi: ",suma/n)