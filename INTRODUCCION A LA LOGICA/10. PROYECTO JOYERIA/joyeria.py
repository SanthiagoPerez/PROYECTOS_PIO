import os

#lista de productos e inventario disponible

productos = [
    {"nombre": "Anillo de diamante","precio": 10000,"cantidad": 5},
    {"nombre": "Anillo de Cuarzo", "precio": 400, "cantidad": 8},
    {"nombre": "Anillo de Plata", "precio": 1000, "cantidad": 12},
    {"nombre": "Anillo de Oro", "precio": 6000, "cantidad": 5}
]

carrito = []

def limpiarPantalla():
    if os.name == 'nt':
        os.system("cls") #limpiar pantalla en windows
    else:
        os.system("clear") #limpiar terminal en linux o mac

def mostrar_productos():
    limpiarPantalla()
    print("-------------MENÚ DE PRODUCTOS---------")
    for i, producto in enumerate(productos):
        print(f"{i+1}.{producto['nombre']} - precio ${producto['precio']} - cantidad{producto['cantidad']}")

def agregar_al_carrito():
    limpiarPantalla()
    mostrar_productos()
    try:
        opcion = int(input("Digite la opcion de el producto que desea agregar: "))
        if 1 <= opcion <= len(productos):
            cantidad = int(input("Digite la cantidad de productos a comprar: "))
            producto = productos[opcion-1]
            if cantidad > producto["cantidad"]:
                print("No hay suficiente existencia del producto")
            else:
                productos[opcion-1]['cantidad']-=cantidad
                carrito.append({"nombre": producto["nombre"], "precio": producto['precio'], "cantidad": cantidad})
                print(f"Felicitaciones añadiste {cantidad}{producto['nombre']} de manera exitosa")
    except Exception as e:
        print("se ha producido un error", e)

def mostrarCarrito():
    limpiarPantalla()
    if carrito:
        print("carrito de compras")
        for i, item in enumerate(carrito, 1):
            print(f"{i}.producto:{item["nombre"]} - ${item["precio"]} - cantidad:{item["cantidad"]}")
    else:
            print("El carrito esta vacio")

def calcularTotal():
    total = sum(item["precio"]*item["cantidad"] for item in carrito)
    print(f"el total a pagar es: ${total}")

def finalizarCompra():
    limpiarPantalla()
    mostrarCarrito()

    if carrito:
        calcularTotal()
        confirmar = int(input("¿Desea finalizar su compra (s/n)"))

        if confirmar.lower() == "s":
            carrito.clear()
            print("La compra fue realizada exitosamente")
        else:
            print("La compra fue cancelada")
    else:
        print("No hay productos en el carrito")
        

def main():
    while True:
        limpiarPantalla()
        print("---------- MENU JOYERIA --------")
        print("1. Mostrar productos disponibles")
        print("2. Añadir productos al carrito")
        print("3. Mostrar carrito")
        print("4. Finalizar compra")
        print("5. Salir de la compra")

        try:
            opciones = {
                1:mostrar_productos,
                2:agregar_al_carrito,
                3:mostrarCarrito,
                4:finalizarCompra
            }

            seleccion = int(input("Digite la opcion deseada: "))
            if seleccion in opciones:
                opciones[seleccion]()
                input("presione enter para continuar")
            elif seleccion == 5:
                break

        except ValueError:
            print("La entrada es invalida, por favor digite un número")
            input("Presione enter para continuas....")

        except Exception:
            print("Se ha presentado un error")
            input("Presione enter para continuar....")

main()