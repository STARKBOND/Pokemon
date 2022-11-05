import sys
import os

mango_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(mango_dir)

from Listen import *

infile = open("pocketsphinx/1827.dic", mode='r')

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

