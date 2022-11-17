values=[10,20,30]
keys=['ten','twenty','thirty']
D={}
for i in range(len(values)):
    #D[klucz] = wartosc
    D[keys[i]]=values[i]
print(D)

D_2={}
D_2=dict(thirty=30,forty=40,fift=50)
print(D_2)
D.update(D_2)
print(D)