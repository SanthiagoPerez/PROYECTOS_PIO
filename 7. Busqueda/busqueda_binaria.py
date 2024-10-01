def busqueda_binaria(lista,objetivo):
    inicio = 0
    fin = len(lista)-1 #empiza desde 0 

    while inicio <= fin:
        medio = (inicio + fin) //2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio +1
        else:
            fin = medio - 1

numeros_ordenados = [i for i in range(1,101)]

resultado = busqueda_binaria(numeros_ordenados,77)

if resultado:
    print("Encontrado", resultado)
else:
    print("Elemento no encontrado")