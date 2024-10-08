'''
Escriba un usuario que pida una calificacion numerica de (0-100)
y determine si el estudiante apruba o no (60 o mas aprobado)
'''
import math
#importan funciones matematicas

calificacion = float(input("Ingrese la calificacion de 0 - 100: "))

#calificacion = round(calificacion)#aproxima el numero (redondeo general)
calificacion = math.floor(calificacion)#piso
calificacion = math.ceil(calificacion)#techo

if calificacion > 100 or calificacion < 0:
    print("La nota es incorrecta")
elif calificacion >= 60 and calificacion <= 100: #se puede omitir desde el and
    print(f"El estudiante Aprobó, NOTA {calificacion}")
else:
    print (f"El estudiante no Aprobó, NOTA {calificacion}")