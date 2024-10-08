#calcular los impuestos

salario = float(input("Ingrese su salario anual: "))

if salario > 0:
    if salario > 50000:
        if salario > 100000:
            print("El impuesto es del 30%")
        else:
            print("El salario es del 20%")
    else:
        print("No paga impuesto")
else:
    print("Salario no valido")