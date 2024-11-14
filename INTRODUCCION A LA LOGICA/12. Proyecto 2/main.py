usuarios = {
    "usuario": {"contrasenia": "123", "saldo": 1000},
    "usuario2": {"contrasenia": "123", "saldo": 5000},
    "usuario3": {"contrasenia": "123", "saldo": 80000},
    "usuario4": {"contrasenia": "123", "saldo": 1000001},
    "usuario5": {"contrasenia": "123", "saldo": 987500},
}

def autenticarUsuario(nombre, contrasenia):
    usuario = usuarios.get(nombre)
    if usuario and usuario.get("contrasenia") == contrasenia:
        return True
    return False

def consultarSaldo(usuario):
    return usuario.get("saldo")

def retirarDinero(usuario, cantidad):
    """
    Retira una cantidad de dinero de la cuenta de un usuario autenticado.

    Primero verifica que la cantidad a retirar sea mayor a 0 y menor o igual al saldo disponible
    en la cuenta del usuario. Si se cumple esta condicion, se resta la cantidad del saldo del usuario
    y se devuelve un mensaje de exito. Si no se cumple, se devuelve un mensaje de error.

    Args:
        usuario (dict): Diccionario con la informacion del usuario del que se va a retirar dinero.
        cantidad (int): Cantidad de dinero a retirar.

    Returns:
        str: Mensaje de exito o error en la retirada de dinero.
    """
    if cantidad > 0:
        if cantidad <= usuario.get("saldo"):
            usuario["saldo"] -= cantidad
            return f"Se han retirado ${cantidad} de tu cuenta"
    return "Saldo insuficiente"

def depositarDinero(usuario, cantidad):
    if cantidad > 0:
        usuario["saldo"] += cantidad
        return f"Se han depositado ${cantidad} en tu cuenta"
    return "La cantidad a depositar debe ser mayor a 0"

# funcion para cambiar la contrasenia
def cambiarContrasenia(usuario):
    """
    Cambia la contrasenia de un usuario autenticado.

    Primero pregunta la contrasenia actual, y si coincide con la del usuario, le permite
    cambiarla por una nueva. Si la contrasenia actual es incorrecta, se devuelve un mensaje
    de error.

    Args:
        usuario (dict): Diccionario con la informacion del usuario a cambiar su contrasenia.

    Returns:
        str: Mensaje de exito o error en el cambio de contrasenia.
    """
    contraseniaActual = input("Ingrese su contrasenia actual: ")
    if contraseniaActual == usuario.get("contrasenia"):
        nuevaContrasenia = input("Ingrese su nueva contrasenia: ")
        usuario["contrasenia"] = nuevaContrasenia
        return f"La contrasenia se ha cambiado con exito"
    return f"La contrasenia actual es incorrecta"
# creacion de menu que me va a permitir autenticar si el usurario esta creado y luego de autenticarlo me va a permitir revisar las opciones de cajero
def menu():
    while True:
        nombre = input("Ingrese su nombre o (exit) para salir: ")
        if nombre.lower() == "exit":
            break
        contrasenia = input("Ingrese su contrasenia: ")
        autenticado = autenticarUsuario(nombre, contrasenia)
        if not autenticado:
            print("Usuario no autenticado")
            continue
        print("Bienvenido al cajero")
        while True:
            print("---------------- MENÚ CAJERO ---------------")
            print("1. Consultar saldo")
            print("2. Retirar")
            print("3. Depositar")
            print("4. Cambiar contrasenia")
            print("5. Salir")
            print("-----------------------------------------------")
            try:
                opcion = int(input("Elija una opcion: "))
                if opcion == 1:
                    print(f"Tu saldo es de ${consultarSaldo(usuarios[nombre])}")
                elif opcion == 2:
                    retiro = float(input("Cuanto deseas retirar: "))
                    print(retirarDinero(usuarios[nombre], retiro))
                elif opcion == 3:
                    deposito = float(input("Cuanto deseas depositar: "))
                    print(depositarDinero(usuarios[nombre], deposito))
                elif opcion == 4:
                    cambiarContrasenia(usuarios[nombre])
                elif opcion == 5:
                    print("Hasta pronto")
                    break
            except Exception as e:
                print("Opcion invalida")
                print(e)

menu()