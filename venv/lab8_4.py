def znaki(napis):
    slownik = {}
    for i in napis:
        if i in slownik:
            slownik[i]=slownik[i]+1
        else:
            slownik[i]=1
    return slownik

napis = input("Podaj stringa: ")
print(znaki(napis))