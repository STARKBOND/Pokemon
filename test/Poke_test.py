from Listen import *

infile = open("pocketsphinx/1827.dic", mode='r')

pokemon = {}

for line in infile:
    pokemon[line.split("\t")[0]] = line.split("\t")[1]

for name in pokemon:
    if "ER" in pokemon[name]:
        print(name)
        if listen() == name:
            print("correct!")
        else:
            print("incorrect!")

