def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i] , lista[min_idx] = lista[min_idx], lista[i]
    return lista



numeros = [51,42,74,1,10]
print(selection_sort(numeros))