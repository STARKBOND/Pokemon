from Listen import *

infile = open("1827.dic", mode='r')

pokemon = {}

for line in infile:
    pokemon[line.split("\t")[0]] = line.split("\t")[1]

for name in pokemon:
    # print(key, pokemon[key])
    if "ER" in pokemon[name]:
        print(name)
        if listen() == name:
            print("correct!")
        else:
            print("incorrect!")

