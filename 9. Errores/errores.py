while True:
    try:
        numero = input("Ingrese su nombre: ")
        telefono = int(input("Ingrese su telefono: "))
        print("Usuario registrado")
        break
    except Exception as e:
        print(f"Dato no valido: {e}")
        print("Intenta de nuevo")