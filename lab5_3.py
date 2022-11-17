#pierwsza metoda
D_1={}
for i in range(1,16):
    D_1[i]=i*i
print(D_1)
D_2={}
for i in range(11):
    D_2[i]=2**i
print(D_2)

#druga metoda
D_1 = {i: i*i for i in range(1,16)}
print(D_1)
D_2 = {i: 2**i for i in range(11)}
print(D_2)