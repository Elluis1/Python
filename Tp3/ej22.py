# creamos la cola
cola_personajes = [
    {"nombre": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"nombre": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
    {"nombre": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"nombre": "Thor Odinson", "superheroe": "Thor", "genero": "M"},
    {"nombre": "Bruce Banner", "superheroe": "Hulk", "genero": "M"},
    {"nombre": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"nombre": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"nombre": "Wanda Maximoff", "superheroe": "Scarlet Witch", "genero": "F"},
    {"nombre": "Peter Parker", "superheroe": "Spider-Man", "genero": "M"},
    {"nombre": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"},
    {"nombre": "Shuri", "superheroe": "Shuri", "genero": "F"},
    {"nombre": "Sam Wilson", "superheroe": "Falcon", "genero": "M"},
]

# Actividad a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
nombre_capitana_marvel = ""
for personaje in cola_personajes:
    if personaje["superheroe"] == "Capitana Marvel":
        nombre_capitana_marvel = personaje["nombre"]
        break  # Salir del bucle una vez encontrado

print("a. Nombre del personaje de la Capitana Marvel:", nombre_capitana_marvel)

# Actividad b. Mostrar los nombres de los superhéroes femeninos
print("b. Nombres de superhéroes femeninos:")
for personaje in cola_personajes:
    if personaje["genero"] == "F":
        print(personaje["superheroe"])

# Actividad c. Mostrar los nombres de los personajes masculinos
print("c. Nombres de personajes masculinos:")
for personaje in cola_personajes:
    if personaje["genero"] == "M":
        print(personaje["nombre"])

# Actividad d. Determinar el nombre del superhéroe del personaje Scott Lang
nombre_scott_lang = ""
for personaje in cola_personajes:
    if personaje["nombre"] == "Scott Lang":
        nombre_scott_lang = personaje["superheroe"]
        break  # Salir del bucle una vez encontrado

print("d. Superhéroe del personaje Scott Lang:", nombre_scott_lang)

# Actividad e. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra S
print("e. Datos de superhéroes cuyos nombres comienzan con S:")
for personaje in cola_personajes:
    if personaje["nombre"][0] == "S":
        print(personaje)

# Actividad f. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroe
carol_danvers_en_cola = False
superheroe_carol_danvers = ""
for personaje in cola_personajes:
    if personaje["nombre"] == "Carol Danvers":
        carol_danvers_en_cola = True
        superheroe_carol_danvers = personaje["superheroe"]
        break  # Salir del bucle una vez encontrado

if carol_danvers_en_cola:
    print("f. Carol Danvers está en la cola. Su superhéroe es:", superheroe_carol_danvers)
else:
    print("f. Carol Danvers no está en la cola.")
