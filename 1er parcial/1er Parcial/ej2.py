from collections import deque

def hallar_pj(character_name, avengers_list):
    for avenger in avengers_list:
        if avenger[0] == character_name:
            return avenger[1]
    return None

def contar_superheroes_en_grupo(group_name, avengers_list):
    superheroes_queue = deque()
    count = 0

    for avenger in avengers_list:
        if avenger[2] == group_name:
            superheroes_queue.append(avenger[0])
            count += 1

    return superheroes_queue, count

def filtrar_pj_por_inicial(characters_list, initials):
    filtered_characters = []

    for character in characters_list:
        if character[0][0].upper() in initials:
            filtered_characters.append(character)

    return filtered_characters

def filtrar_superheroes_por_grupo(group_name, avengers_list):
    superheroes = []

    for avenger in avengers_list:
        if avenger[2] == group_name:
            superheroes.append(avenger[0])

    return sorted(superheroes, reverse=True)

def filtrar_superheroes_por_año(avengers_list, min_year):
    superheroes = []

    for avenger in avengers_list:
        if avenger[3] > min_year:
            superheroes.append(avenger[0])

    return superheroes

def corregir_nombre_superheroe(avengers_list, wrong_name, correct_name):
    for i, avenger in enumerate(avengers_list):
        if avenger[0] == wrong_name:
            avengers_list[i] = (correct_name, avenger[1], avenger[2], avenger[3])

def añadir_pj_a_la_lista(aux_list, avengers_list):
    for character in aux_list:
        character_name = character[0]
        exists = False

        for avenger in avengers_list:
            if avenger[0] == character_name:
                exists = True
                break

        if not exists:
            avengers_list.append(character)

avengers = [
    ("Iron Man", "Tony Stark", "Vengadores", 1963),
    ("Capitán América", "Steve Rogers", "Vengadores", 1941),
    ("Thor", "", "Vengadores", 1962),
    ("Vlanck Widow", "Natasha Romanoff", "Vengadores", 1964),
    ("Ojo de Halcón", "Clint Barton", "Vengadores", 1964),
    ("Capitana Marvel", "Carol Danvers", "Vengadores", 1968),
    ("Ant-Man", "Scott Lang", "Vengadores", 1962),
    ("Spider-Man", "Peter Parker", "", 1962),
    ("Star Lord", "Peter Quill", "Guardianes de la galaxia", 1976),
    ("Gamora", "", "Guardianes de la galaxia", 1975),
    ("Drax", "Drax el Destructor", "Guardianes de la galaxia", 1973),
    ("Rocket Raccoon", "", "Guardianes de la galaxia", 1976),
    ("Groot", "", "Guardianes de la galaxia", 1960),
    ("Nebula", "", "Guardianes de la galaxia", 1985),
    ("Sr. Fantástico", "Reed Richards", "Los cuatro fantásticos", 1961),
    ("Mujer Invisible", "Sue Storm", "Los cuatro fantásticos", 1961),
    ("Antorcha Humana", "Johnny Storm", "Los cuatro fantásticos", 1961),
    ("La Cosa", "Ben Grimm", "Los cuatro fantásticos", 1961)
]

corregir_nombre_superheroe(avengers, "Vlanck Widow", "Black Widow")

auxiliar = [
    ('Black Cat', 'Felicia Hardy', '', 1979 ),
    ('Hulk', 'Robert Bruce Banner', 'Vengadores', 1962),
    ('Rocket Racoonn', '', '', 0),
    ('Loki', 'Loki Laufeyson', '', 1949)
]

añadir_pj_a_la_lista(auxiliar, avengers)


character_name = "Capitana Marvel"
character = hallar_pj(character_name, avengers)

if character is not None:
    print(f"El nombre de personaje de {character_name} es: {character}.")
else:
    print(f"{character_name} no se encuentra en la lista.")


group_names = ["Los cuatro fantásticos", "Guardianes de la galaxia"]

for group_name in group_names:
    superheroes_group = filtrar_superheroes_por_grupo(group_name, avengers)
    print(f"Superhéroes del grupo '{group_name}' (en orden descendente):")
    for superhero in superheroes_group:
        print(superhero)
    print()

group_name = "Guardianes de la galaxia"
superheroes_queue, count = contar_superheroes_en_grupo(group_name, avengers)

print(f"Los superhéroes que pertenecen al grupo '{group_name}' son:")
for superhero in superheroes_queue:
    print(superhero)

print(f"Total: {count}")

min_year = 1960
superheroes = filtrar_superheroes_por_año(avengers, min_year)

print(f"Superhéroes cuyo nombre de personaje tiene un año de aparición posterior a {min_year}:")
for superhero in superheroes:
    print(superhero)

initials = ['C', 'P', 'S']
characters_starting_with_initials = filtrar_pj_por_inicial(avengers, initials)

print("Personajes que comienzan con C, P o S:")
for character in characters_starting_with_initials:
    print(character)



