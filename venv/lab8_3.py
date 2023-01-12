def potega(l1,l2):
    lista=[]
    if len(l1)==len(l2):
        for i in range(len(l1)):
            lista.append(l1[i]**l2[i])
    return lista


l1=[1,2,3,4,5]
l2=[3,3,3,3,3]
print(potega(l1,l2))