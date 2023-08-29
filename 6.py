class Superhero:
    def __init__(self, name, year, comic_house, biography):
        self.name = name
        self.year = year
        self.comic_house = comic_house
        self.biography = biography

# Crear una lista de objetos Superhero con la información dada
superheroes = [
    Superhero("Spider-Man", 1962, "Marvel", "Biografía de Spider-Man..."),
    Superhero("Batman", 1939, "DC", "Biografía de Batman..."),
    Superhero("Superman", 1938, "DC", "Biografía de Superman..."),
    Superhero("Linterna Verde", 1940, "DC", "Biografía de Linterna Verde..."),
    Superhero("Wolverine", 1974, "Marvel", "Biografía de Wolverine..."),
    Superhero("Dr. Strange", 1963, "Marvel", "Biografía de Dr. Strange..."),
    Superhero("Iron Man", 1963, "Marvel", "Biografía de Iron Man..."),
    Superhero("Capitana Marvel", 1968, "Marvel", "Biografía de Capitana Marvel..."),
    Superhero("Mujer Maravilla", 1941, "DC", "Biografía de Mujer Maravilla..."),
    Superhero("Flash", 1940, "DC", "Biografía de Flash..."),
    Superhero("Star-Lord", 1976, "Marvel", "Biografía de Star-Lord...")
]

def remove_superhero(name):
    global superheroes
    superheroes = [hero for hero in superheroes if hero.name != name]

def year_of_appearance(name):
    for hero in superheroes:
        if hero.name == name:
            return hero.year

def change_comic_house(name, new_comic_house):
    for hero in superheroes:
        if hero.name == name:
            hero.comic_house = new_comic_house

def find_keywords_in_biography(keyword_list):
    return [hero.name for hero in superheroes if any(keyword in hero.biography.lower() for keyword in keyword_list)]

def superheroes_before_year(year):
    return [(hero.name, hero.comic_house) for hero in superheroes if hero.year < year]

def find_comic_house(*hero_names):
    comic_houses = {}
    for hero_name in hero_names:
        for hero in superheroes:
            if hero.name == hero_name:
                comic_houses[hero.name] = hero.comic_house
                break
    return comic_houses

def get_superhero_info(name):
    for hero in superheroes:
        if hero.name == name:
            return vars(hero)

def superheroes_starting_with_letters(*letters):
    return [hero.name for hero in superheroes if hero.name.startswith(letters)]

def count_superheroes_by_comic_house():
    comic_house_count = {"Marvel": 0, "DC": 0}
    for hero in superheroes:
        comic_house_count[hero.comic_house] += 1
    return comic_house_count

# Actividad a. Eliminar el nodo de Linterna Verde
remove_superhero("Linterna Verde")

# Actividad b. Mostrar el año de aparición de Wolverine
print(year_of_appearance("Wolverine"))

# Actividad c. Cambiar la casa de Dr. Strange a Marvel
change_comic_house("Dr. Strange", "Marvel")

# Actividad d. Mostrar superhéroes con "traje" o "armadura" en la biografía
print(find_keywords_in_biography(["traje", "armadura"]))

# Actividad e. Mostrar superhéroes anteriores a 1963
print(superheroes_before_year(1963))

# Actividad f. Mostrar la casa de Capitana Marvel y Mujer Maravilla
print(find_comic_house("Capitana Marvel", "Mujer Maravilla"))

# Actividad g. Mostrar la información de Flash y Star-Lord
print(get_superhero_info("Flash"))
print(get_superhero_info("Star-Lord"))

# Actividad h. Listar superhéroes que comienzan con B, M y S
print(superheroes_starting_with_letters("B", "M", "S"))

# Actividad i. Contar superhéroes por casa de comic
print(count_superheroes_by_comic_house())
