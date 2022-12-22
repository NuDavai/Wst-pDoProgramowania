import numpy as np

macierz = np.random.randint(low=0 , high=100 , size=(5,5))
print(macierz)

print(f"wartość maksymalna: {macierz.max()}")
print(f"wartość minimalna: {macierz.min()}")

print(f"wartość maksymalna dla wierszów: {macierz.max(axis=1)}")
print(f"wartość minimalna dla wierszów: {macierz.min(axis=1)}")

print(f"wartość maksymalna dla kolumn: {macierz.max(axis=0)}")
print(f"wartość minimalna dla kolumn: {macierz.min(axis=0)}")

print(f"suma w wierszach: {macierz.sum(axis=1)}")
print(f"suma w kolumnach: {macierz.sum(axis=0)}")