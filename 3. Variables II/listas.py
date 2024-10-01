'''
listas son colecciones de datos ordenados y mutables(cambiar su valor)
pueden almacenar elementos de cualquier tipo

CARACTERISTICAS
  * Son ordenadas
  * Son mutables
  * Pueden contener elementos duplicados
  * los elementos pueden ser de diferentes tipos de datos
'''

#Definicion de una lista
mi_lista = [10, 20, 30, 40, "Hola"]
print(mi_lista)

#acceder a un elemento
print(mi_lista[3])

#modificar un elemento
mi_lista[3] = "adios"
print(mi_lista)

#agregar elementos a la lista
mi_lista.append(50)
print(mi_lista)

#eliminar un elemento
mi_lista.remove(10) #opcion 1 busqueda
#mi_lista.remove(mi_lista[0])#opcion 2
print(mi_lista)

#Contador (Longitud)
print(len(mi_lista))

'''
#Operadores
append(): Agrega un elemento al final
remove(): Elimina el primer elemento que coincide con el valor
len(): Devuelve la longitud de la lista
'''