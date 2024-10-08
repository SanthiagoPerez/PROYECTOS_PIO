def busqueda_lineal(objeto,lista):
    for i in range(len(lista)):
        if lista[i] == objeto:
            return i #devuelve el indice del elemento
        
#ejemplo de uso
numeros = [10,20,30,45,90,11,22]

resultado = busqueda_lineal(45,numeros)

if resultado:
    print("Elemento Encontrado")

else:
    print("Elemento no Encontrado")