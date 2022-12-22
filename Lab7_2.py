import numpy as np

potegi2 = []
for i in range(7,-1,-1):
    potegi2.append(2**i)
print(potegi2)

wagi = np.array(potegi2)
print(wagi)

liczba_bin = np.random.randint(low=0, high=2, size=8)
print(liczba_bin)

iloczyn = liczba_bin * wagi
print(iloczyn)

suma = 0
for i in range(8):
    suma = suma + iloczyn[i]
print(suma)
print(iloczyn.sum())