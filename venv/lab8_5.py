def dodawanie(a,b):
    return a + b
def odejmowanie(a,b):
    return a - b
def mnozenie(a,b):
    return a * b
def dzielenie(a,b):
    if b==0:
        return None
    else:
        return a / b

dzialania = {"+":dodawanie,"-":odejmowanie,"*":mnozenie,"/":dzielenie}

x = input("Jakie dzialanie wariacie? (+,-,*,/) : ")
a = int(input("Podaj a:"))
b = int(input("Podaj b:"))
print(dzialania[x](a,b))