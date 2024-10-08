#evaluar una condicion dentro de otra condicion

'''if condicion1:
    #Bloque de codigo si condicion1 es verdadera
    if condicion2:
        #bloque de codigo si la condicion2 es verdadera(pero condicion1 es verdadera)
    else:
        #bloque de codigo si condicion2 es falsa(pero condicion1 es verdadera)
else:
    #bloque de codigo si condicion1 es falsa
'''

edad = 20
tiene_licencia = True

if edad >= 18:
    print("Eres mayor de edad")
    
    if tiene_licencia:
        print("Tiene licencia de conducir, puede manejar")
    else:
        print()