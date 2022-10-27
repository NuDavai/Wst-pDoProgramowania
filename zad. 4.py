x = int(input("podaj pierwsza liczbe: "))
y = int(input("podaj druga liczbe: "))

if x>y:
    (x,y) = (y,x) #krotka

print("pierwsza liczba: ",x)
print("druga liczba: ",y)

print(x)

while x<y:
    x = x + 1
    if x%2!=0:
        continue
    print(x)
