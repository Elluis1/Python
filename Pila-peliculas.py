peliculas = [
    {"titulo": "Avengers: Age of Ultron", "estudio": "Marvel Studios", "anio": 2015},
    {"titulo": "Captain America: Civil War", "estudio": "Marvel Studios", "anio": 2016},
    {"titulo": "Black Panther", "estudio": "Marvel Studios", "anio": 2018},
    {"titulo": "Spider-Man: Homecoming", "estudio": "Sony Pictures", "anio": 2017},
    {"titulo": "The Avengers", "estudio": "Marvel Studios", "anio": 2012},
    {"titulo": "Star Wars: The Force Awakens", "estudio": "Lucasfilm", "anio": 2015},
    {"titulo": "Wonder Woman", "estudio": "DC Films", "anio": 2017},
    {"titulo": "Deadpool", "estudio": "20th Century Fox", "anio": 2016},
    {"titulo": "Jurassic World", "estudio": "Universal Pictures", "anio": 2015},
    {"titulo": "The Dark Knight Rises", "estudio": "Warner Bros.", "anio": 2012},
    {"titulo": "Guardians of the Galaxy", "estudio": "Marvel Studios", "anio": 2014},
    {"titulo": "Captain America: The Winter Soldier", "estudio": "Marvel Studios", "anio": 2014},
    {"titulo": "X-Men: Days of Future Past", "estudio": "20th Century Fox", "anio": 2014}
]

def peliculas_de_anio(peliculas, anio):
    pila = []
    for pelicula in peliculas:
        if pelicula["anio"] == anio:
            pila.append(pelicula["titulo"])
    return pila

def cantidad_de_peliculas_de_anio(peliculas, anio):
    pila = []
    for pelicula in peliculas:
        if pelicula["anio"] == anio:
            pila.append(pelicula["titulo"])
    return len(pila)

def peliculas_de_marvel_de_anio(peliculas, anio):
    pila = []
    for pelicula in peliculas:
        if pelicula["anio"] == anio and pelicula["estudio"] == "Marvel Studios":
            pila.append(pelicula["titulo"])
    return pila

peliculas_2014 = peliculas_de_anio(peliculas, 2014)
peliculas_2018 = cantidad_de_peliculas_de_anio(peliculas, 2018)
peliculas_de_marvel_2016 = peliculas_de_marvel_de_anio(peliculas, 2016)

print("Estas son las peliculas estrenadas en 2014: ", peliculas_2014)
print("¿Cuantas son las peliculas estrenadas en 2018? Esta cantidad: ", peliculas_2018)
print("Estas son las peliculas de marvel estrenadas en 2016: ", peliculas_de_marvel_2016)