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

# listen() could be an event that Question is listening to
# Question could have 2 types
    # What is <stat> <type/pokemon>?
    # What (does/is) <type/pokemon> <stat>?
# Each with a corresponding event handler
    # if SUBSTRING(first 3 words of question) in "what is" or "what's" in 
        # if SUBSTRING(the rest of the question) in <type>
            # create type
            # or if SUBSTRING(the rest of the question) in <type> <type>
                # create dualType
        # if SUBSTRING(the rest of the question) in <pokemon>
            # spawn pokemon
