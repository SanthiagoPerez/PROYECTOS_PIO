
directores = [{
    "nombre": "Christopher Nolan",
    "edad": 51,
    "genero": "Masculino",
},
    {
    "nombre": "Martin Scorsese",
    "genero": "Masculino",
    "edad": 70
},
    {
    "nombre": "Quentin Tarantino",
    "genero": "Masculino",
    "edad": 55
}
]

peliculas = [{
    "nombre": "Interstellar",
    "director": "Christopher Nolan",
    "duracion": 160,
    "genero": ['Crimen', 'Drama'],
    "clasificacion": "B15"
},

    {
    "nombre": "Inception",
    "director": "Christopher Nolan",
    "duracion": 148,
    "genero": ['Aventura'],
    "clasificacion": "B15"
},
{
    "nombre": "Pulp Fiction",
    "director": "Quentin Tarantino",
    "duracion": 154,
    "genero": ['Crimen', 'Drama'],
    "clasificacion": "B15"}
]

roles = [{
    "usarname": "admin",
    "password": "admin123",
    "permisos": True,
    "reservas": []
},
{
    "usarname": "user",
    "password": "user123",
    "permisos": False,
    "reservas": []
}]

salas = [{
    "nombre": "Sala 1",
    "pelicula": 0,
    "capacidad": 100
},
{
    "nombre": "Sala 2",
    "pelicula": 1,
    "capacidad": 200
}]

reservas = []

def mostrar_todas_peliculas(peliculas):
    print("------ LISTA DE PELICULAS ------")
    for pelicula in peliculas:
        print(f"Nombre: {pelicula['nombre']}")
        print(f"Director: {pelicula['director']}")  
        print(f"Duracion: {pelicula['duracion']} minutos")
        print(f"Genero: {', '.join(pelicula['genero'])}")
        print(f"Clasificacion: {pelicula['clasificacion']}")
        print("----------------------")

mostrar_todas_peliculas(peliculas)

def crear_pelicula():
    print("------ Lista de Directores ------")
    for i, director in enumerate(directores):
        print(f"{i+1}. {director['nombre']}")
    director = int(input("Elija el director: ")) - 1
    nombre = input("Ingrese el nombre de la Pelicula: ")
    duracion = int(input("Ingrese la duracion de la Pelicula: "))
    genero = input("Ingrese el genero de la Pelicula: ")
    clasificacion = input("Ingrese la clasificacion de la Pelicula: ")
    peliculas.append ({
        "nombre": nombre,
        "director": directores[director]["nombre"],
        "duracion": duracion,
        "genero": genero,
        "clasificacion": clasificacion
    })

def mostrar_una_pelicula():
    print("------ Lista de Peliculas ------")
    for i, pelicula in enumerate(peliculas):
        print(f"{i+1}. {pelicula['nombre']}")
    indice = int(input("Elija una Pelicula: ")) - 1
    print(f"Nombre: {peliculas[indice]['nombre']}")
    print(f"Director: {peliculas[indice]['director']}")
    print(f"Duracion: {peliculas[indice]['duracion']} minutos")
    print(f"Genero: {', '.join(peliculas[indice]['genero'])}")
    print(f"Clasificacion: {peliculas[indice]['clasificacion']}")
    print("----------------------")

def mostrar_todos_directores():
    print("------ Lista de Directores ------")
    for director in directores:
        print(f"Nombre: {director['nombre']}")
        print(f"Edad: {director['edad']}")
        print(f"Genero: {director['genero']}")
        print("----------------------")

def crear_director():
    nombre = input("Ingrese el nombre del director: ")
    edad = int(input("Ingrese la edad del director: "))
    genero = input("Ingrese el genero del director: ")
    directores.append ({
        "nombre": nombre,
        "edad": edad,
        "genero": genero
    })

def mostrar_un_director():
    print("------ Lista de Directores ------")
    for i, director in enumerate(directores):
        print(f"{i+1}. {director['nombre']}")
    indice = int(input("Elija un director: ")) - 1
    print(f"Nombre: {directores[indice]['nombre']}")
    print(f"Edad: {directores[indice]['edad']}")
    print(f"Genero: {directores[indice]['genero']}")
    print("----------------------")

def login(usarname, password):
    for role in roles:
        if role["usarname"] == usarname and role["password"] == password:
            return role

def comprar_ticket():
    print("------ Comprar Ticket ------")
    print(f"Salas":)

def menu():
    usarname = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contrasenia: ")
    role = login(usarname, password)
    if role:
        print("Inicio de sesión exitoso")
        
        if role["permisos"]:
            while True:
                print("---------------- MENÚ ADMINISTRADOR ---------------")
                print("1. Crear Pelicula")
                print("2. Mostrar Una Pelicula")
                print("3. Mostrar Todas las Peliculas")
                print("4. Crear Director")
                print("5. Mostrar Un Director")
                print("6. Mostrar Todos los Directores")
                print("7. Salir")
                print("-----------------------------------------------")
                try:
                    opcion = int(input("Elija una opcion: "))
                    if opcion == 1:
                        crear_pelicula()
                    elif opcion == 2:
                        mostrar_una_pelicula()
                    elif opcion == 3:
                        mostrar_todas_peliculas(peliculas)
                    elif opcion == 4:
                        crear_director()
                    elif opcion == 5:
                        mostrar_un_director()
                    elif opcion == 6:
                        mostrar_todos_directores()
                    elif opcion == 7:
                        break
                except ValueError:
                    print("Opcion no valida")