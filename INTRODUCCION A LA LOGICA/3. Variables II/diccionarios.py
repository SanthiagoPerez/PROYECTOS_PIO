'''
DICCIONARIOS

Un diccionario es una coleccion desordenada de pares Clave-Valor, donde
cada clave es unica y estar asociada a un valor. se utilizan para representaciones
de datos, como una tabla

CARACTERISTICAS
  * Los elementos se almacenas como pares clave-valor
  * Son mutables
  * las claves son unicas, no puede ser repetidas pero los valores si se pueden repetir
  * las claves son inmutables
'''

#Definicion de un diccionario
mi_diccionario = {
    "nombre": "Santiago",
    "edad": 24,
    "ciudad": "Tulua",
    "idiomas": ["ingles", "Español", "frances"],
    "Grupo sanguineo": None
}
print(mi_diccionario["idiomas"][2])

#acceder a un valor
print(mi_diccionario["ciudad"])

#modificar un valor
mi_diccionario["edad"] = 27
print(mi_diccionario["edad"])

#agregar un nuevo par de clave-valor
mi_diccionario["profession"] = "ingeniero"
print(mi_diccionario)

#eliminar un par de clave-valor
del mi_diccionario["ciudad"]
print(mi_diccionario)

'''
Operadores
 * del: eliminara un par de clave-valor
'''