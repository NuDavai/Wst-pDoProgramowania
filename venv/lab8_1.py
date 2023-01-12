def find(lista, wartosc):
    indeksy=[]
    for i in range(len(lista)):
        if lista[i] == wartosc:
            indeksy.append(i)
    return indeksy

print(find([1,2,3,4,5,6,7,8,9,10],5))

l =[1,2,4,8,16,32,64]