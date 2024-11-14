peliculas = [
    {"nombre": "Joker: Folie à Deux", "descripcion": "Secuela de Joker (2019), de nuevo con Phoenix como Arthur Fleck, y que muestra su relación con el personaje de Harley Quinn, interpretado por Lady Gaga.",
     "estreno": "03-Oct-2024",
     "genero": ["Drama", "Secuela", "Thriller"], "clasificacion": "Exclusiva para mayores de 15 años",
     "duracion": 138,
     "director": "Todd Phillips",
     "actores": ["Joaquin Phoenix", "Lady Gaga", "Brendan Gleeson"]
     }
]

def mostrar_todas_peliculas(peliculas):
    print("------ LISTA DE PELICULAS ------")
    for pelicula in peliculas:
        print(f"Nombre: {pelicula['nombre']}")

def actualizar_una_pelicula(id_actualizar, pelicula):
    for indice, pelicula in enumerate (peliculas):
        if id_actualizar == indice:
            print("pelicula encontrada")
            nombre = input(f"Ingrese nuevo Nombre de la pelicula({pelicula['nombre']})")

mostrar_todas_peliculas(peliculas)