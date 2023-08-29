class Pokemon:
    def __init__(self, name, level, p_type, sub_type):
        self.name = name
        self.level = level
        self.p_type = p_type
        self.sub_type = sub_type

class Trainer:
    def __init__(self, name, tournaments_won, battles_lost, battles_won, pokemons):
        self.name = name
        self.tournaments_won = tournaments_won
        self.battles_lost = battles_lost
        self.battles_won = battles_won
        self.pokemons = pokemons

# Crear entrenadores y sus pokémons
trainers = [
    Trainer("Ash", 5, 10, 15, [Pokemon("Pikachu", 30, "Eléctrico", None), Pokemon("Charmander", 20, "Fuego", None)]),
    Trainer("Misty", 3, 5, 8, [Pokemon("Starmie", 35, "Agua", "Psíquico"), Pokemon("Psyduck", 25, "Agua", None)]),
    Trainer("Brock", 4, 7, 12, [Pokemon("Onix", 40, "Roca", "Tierra"), Pokemon("Geodude", 15, "Roca", "Tierra")])
]

def count_pokemons(trainer_name):
    for trainer in trainers:
        if trainer.name == trainer_name:
            return len(trainer.pokemons)

def trainers_with_more_than_three_tournaments():
    return [trainer.name for trainer in trainers if trainer.tournaments_won > 3]

def highest_level_pokemon_of_most_successful_trainer():
    most_successful_trainer = max(trainers, key=lambda trainer: trainer.tournaments_won)
    highest_level_pokemon = max(most_successful_trainer.pokemons, key=lambda pokemon: pokemon.level)
    return highest_level_pokemon

def get_trainer_info(trainer_name):
    for trainer in trainers:
        if trainer.name == trainer_name:
            return vars(trainer)

def high_win_percentage_trainers():
    high_win_percentage_trainers = []
    for trainer in trainers:
        win_percentage = trainer.battles_won / (trainer.battles_won + trainer.battles_lost)
        if win_percentage > 0.79:
            high_win_percentage_trainers.append(trainer.name)
    return high_win_percentage_trainers

def fire_plant_or_water_flying_trainers():
    return [trainer.name for trainer in trainers if any(pokemon.p_type == "Fuego" and (pokemon.sub_type == "Planta" or pokemon.sub_type == "Agua/Volador") for pokemon in trainer.pokemons)]

def average_pokemon_level(trainer_name):
    for trainer in trainers:
        if trainer.name == trainer_name:
            pokemon_count = len(trainer.pokemons)
            total_level = sum(pokemon.level for pokemon in trainer.pokemons)
            return total_level / pokemon_count if pokemon_count > 0 else 0

def trainers_with_specific_pokemon(pokemon_name):
    return [trainer.name for trainer in trainers if any(pokemon.name == pokemon_name for pokemon in trainer.pokemons)]

def has_pokemon(trainer_name, pokemon_name):
    for trainer in trainers:
        if trainer.name == trainer_name:
            for pokemon in trainer.pokemons:
                if pokemon.name == pokemon_name:
                    return True, trainer, pokemon
            return False, None, None

# Actividad a. Cantidad de Pokémons de un entrenador
print(count_pokemons("Ash"))

# Actividad b. Entrenadores con más de tres torneos ganados
print(trainers_with_more_than_three_tournaments())

# Actividad c. Pokémon de mayor nivel del entrenador más exitoso
print(highest_level_pokemon_of_most_successful_trainer().name)

# Actividad d. Mostrar todos los datos de un entrenador y sus Pokémons
print(get_trainer_info("Misty"))

# Actividad e. Entrenadores con porcentaje de victorias mayor al 79%
print(high_win_percentage_trainers())

# Actividad f. Entrenadores con tipos de Pokémon específicos
print(fire_plant_or_water_flying_trainers())

# Actividad g. Promedio de nivel de los Pokémons de un entrenador
print(average_pokemon_level("Ash"))

# Actividad h. Cantidad de entrenadores con un Pokémon específico
print(len(trainers_with_specific_pokemon("Pikachu")))

# Actividad i. Entrenadores con Pokémons repetidos
def trainers_with_repeated_pokemons():
    repeated_pokemon_trainers = []
    seen_pokemons = set()
    for trainer in trainers:
        for pokemon in trainer.pokemons:
            if pokemon.name in seen_pokemons:
                repeated_pokemon_trainers.append(trainer.name)
            else:
                seen_pokemons.add(pokemon.name)
    return repeated_pokemon_trainers

print(trainers_with_repeated_pokemons())

# Actividad j. Entrenadores con ciertos Pokémons
print(trainers_with_specific_pokemon("Tyrantrum") + trainers_with_specific_pokemon("Terrakion") + trainers_with_specific_pokemon("Wingull"))

# Actividad k. Verificar si un entrenador tiene un Pokémon específico
trainer_name = "Ash"
pokemon_name = "Pikachu"
has_pokemon_result, trainer, pokemon = has_pokemon(trainer_name, pokemon_name)
if has_pokemon_result:
    print(f"{trainer_name} tiene a {pokemon_name} con los siguientes datos:")
    print(f"Entrenador: {vars(trainer)}")
    print(f"Pokémon: {vars(pokemon)}")
else:
    print(f"{trainer_name} no tiene a {pokemon_name}")
