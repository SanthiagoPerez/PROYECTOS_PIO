def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
           if lista[j] > lista[j+1]:
               apoyo = lista[j]
               lista[j] = lista[j+1]
               lista[j+1] = apoyo
    return lista 

numeros = [6,2,1,4,2,3,8,5,151,23,12,45]
burbuja(numeros)

print(numeros)