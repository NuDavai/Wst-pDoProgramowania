def sum_of_values(dict):
    suma = 0
    for i in dict.values():
        suma = suma + i
    return suma
print(sum_of_values({ "data1" : 1 , "data2" : 2 , "data3" : 3 , "data4" : 4 }))