
# TO DO: avoid sys path hacks, and build package to do relative imports
import sys, os
[sys.path.append(i) for i in ['.', './src/pokemon_nerd']] # allow imports from root dir

from setup import DATA_DIR
from Listen import *

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

