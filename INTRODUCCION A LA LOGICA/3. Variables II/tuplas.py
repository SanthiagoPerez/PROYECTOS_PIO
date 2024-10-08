'''
TUPLAS son colecciones de datos ordenados pero inmutables(no cambian su valor)
pueden almacenar elementos de cualquier tipo

CARACTERISTICAS
  * Son ordenadas
  * Son inmutables
  * Pueden contener elementos duplicados
  * los elementos pueden ser de diferentes tipos de datos
'''

#Definicion de una tupla
mi_tupla = (10, 20, 30, 40, "hola")

#Acceder a un elemento
print(mi_tupla[2])

#intentar modificar un elemento
#mi_tupla[1] = 40 #esto genera un error_ TypeError

#Longitud de una tupla
print(len(mi_tupla))