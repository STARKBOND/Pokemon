from pokemon_nerd.paths import DATA_DIR
from pokemon_nerd.core import *

dictionary_path = os.path.join(DATA_DIR, 'pocketsphinx/1827.dic') 

infile = open(dictionary_path, mode='r')

pokemon = {}

for line in infile:
    pokemon[line.split("\t")[0]] = line.split("\t")[1]

for name in pokemon:
    if "ER" in pokemon[name]:
        print(name)
        res = listen()
        print(res)
        if res == name:
            print("correct!")
        else:
            print("incorrect!")

