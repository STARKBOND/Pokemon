import csv
from PokemonTypes import *

with open('data/pokemon.csv', mode='r') as infile:
    reader = csv.reader(infile)
    next(reader, None)
    pokemon_data = {rows[1]:rows[2:] for rows in reader}

def SpawnPokemon(name: str):
    type = [t for t in pokemon_data[name] if t != '']
    if len(type) == 1:
        pokemon = globals()[type[0]]()
    if len(type) == 2:
        pokemon = globals()[type[0]]() + globals()[type[1]]()
    
    return pokemon
