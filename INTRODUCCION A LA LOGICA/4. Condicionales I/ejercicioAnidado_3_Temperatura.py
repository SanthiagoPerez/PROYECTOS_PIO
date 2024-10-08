temperatura = float(input("Ingrese la Temperatura: "))
clima = input("¿Está lloviendo? (SI_ NO_): ").lower()

if temperatura < 15:
    if clima == "SI":
        print("Usa un abrigo y paraguas")
    else:
        print("Usa un abrigo")
elif 15 <= temperatura <= 25:
    if clima == "SI":
        print("Lleva un paraguas")
    else:
        print("Usa ropa ligera")
else:
    print("Usa ropa fresca")