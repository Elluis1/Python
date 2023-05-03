import pila;

mcu_personajes = [
    {"nombre": "Iron Man", "peliculas": 3},
    {"nombre": "Capitán América", "peliculas": 3},
    {"nombre": "Thor", "peliculas": 4},
    {"nombre": "Hulk", "peliculas": 2},
    {"nombre": "Black Widow", "peliculas": 8},
    {"nombre": "Hawkeye", "peliculas": 5},
    {"nombre": "Spider-Man", "peliculas": 3},
    {"nombre": "Doctor Strange", "peliculas": 2},
    {"nombre": "Black Panther", "peliculas": 1},
    {"nombre": "Ant-Man", "peliculas": 3},
    {"nombre": "Wasp", "peliculas": 2},
    {"nombre": "Captain Marvel", "peliculas": 1},
    {"nombre": "Scarlet Witch", "peliculas": 4},
    {"nombre": "Vision", "peliculas": 3},
    {"nombre": "Falcon", "peliculas": 5},
    {"nombre": "Winter Soldier", "peliculas": 4},
    {"nombre": "War Machine", "peliculas": 5},
    {"nombre": "Groot", "peliculas": 3},
    {"nombre": "Rocket", "peliculas": 3},
    {"nombre": "Gamora", "peliculas": 3},
    {"nombre": "Drax", "peliculas": 3},
    {"nombre": "Nebula", "peliculas": 3},
    {"nombre": "Mantis", "peliculas": 3},
    {"nombre": "Star-Lord", "peliculas": 3}
]

posicion_rocket = None
posicion_groot = None

for i in range(len(mcu_personajes)):
    if mcu_personajes[i]["nombre"] == "Rocket Racoon":
        posicion_rocket = i + 1
    elif mcu_personajes[i]["nombre"] == "Groot":
        posicion_groot = i + 1

print("Rocket Raccoon se encuentra en la posición:", posicion_rocket)
print("Groot se encuentra en la posición:", posicion_groot)

pila = []

for i in mcu_personajes:
    if i["peliculas"] >= 5:
       pila.append((i["nombre"], i["peliculas"]))

for i in pila:
    print(i[0], "aparece en", i[1], "películas.")


for i in mcu_personajes:
    if i["nombre"] == "Black Widow":
       print("Black Widow aparece en: ", i["peliculas"])

Letras_importantes = {"C", "D", "G"}

for i in mcu_personajes:
    if i["nombre"][0] in Letras_importantes:
        print(i["nombre"])






