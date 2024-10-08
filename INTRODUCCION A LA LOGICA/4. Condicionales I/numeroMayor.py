numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))

if numero1 > numero2:
    print(f"El primer numero {numero1}, es mayor que el segundo numero {numero2}")
elif numero1 < numero2:
    print(f"El segundo numero {numero2}, es mayor que el primer numero {numero1}")
else:
    print(f"Ambos numeros son iguales")