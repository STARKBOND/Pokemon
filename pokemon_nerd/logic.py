from pokemon_nerd.core import read_csv
from pokemon_nerd.paths import CSV_PATH
from pokemon_nerd.PokemonType import *
from pokemon_nerd.core import *

pokemon_data = read_csv(CSV_PATH)

def spawn_pokemon(name: str):
    name = name.title()
    type = [t for t in pokemon_data[name] if t != '']
    if len(type) == 1:
        pokemon = globals()[type[0]]()
    if len(type) == 2:
        pokemon = globals()[type[0]]() + globals()[type[1]]()
    
    return pokemon
