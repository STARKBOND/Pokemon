from abc import ABCMeta, abstractmethod
import types

class PokemonType(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.strong_against = None
        self.weak_against = None
        self.resists = None
        self.vulnerable_to = None
        self.immune_against = None
        self.immune_from = None
        self.type = [type(self)]
        self.attrs = getattrs(self)

    def __add__(self, other):
        strong_against, weak_against = combine_stat(self, other, "strong_against", "weak_against")
        resists, vulnerable_to = combine_stat(self, other, "resists", "vulnerable_to")
        immune_against, immune_from = combine_stat(self, other, "immune_against", "immune_from")
        dualType = DualType(type(self), type(other))
        dualType.strong_against = strong_against
        dualType.weak_against = weak_against
        dualType.resists = resists
        dualType.vulnerable_to = vulnerable_to
        dualType.immune_against = immune_against
        dualType.immune_from = immune_from
        handle_immune(dualType)

        return dualType

    def info(self):
        if len(self.type) == 1:
            print("Type: ", end="")
        elif len(self.type) == 2:
            print("DualType: ", end="")
        print_str_tuple(self.type)
        print("Strong against: ", end="")
        print_str_dict(self.strong_against)
        print("Weak against: ", end="")
        print_str_dict(self.weak_against)
        print("Vulnerable to: ", end="")
        print_str_dict(self.vulnerable_to)
        print("Resists: ", end="")
        print_str_dict(self.resists)
        print("Immune from: ", end="")
        print_str_dict(self.immune_from)
        print("Doesn't affect: ", end="")
        print_str_dict(self.immune_against)
        print()
        
class DualType(PokemonType):
    def __init__(self, poke_t1: PokemonType, poke_t2: PokemonType):
        super(DualType, self).__init__()
        self.type = poke_t1, poke_t2

class Normal(PokemonType):
    def __init__(self):
        super(Normal, self).__init__()
        self.weak_against = init_stats([Rock, Steel])
        self.vulnerable_to = init_stats([Fighting])
        self.immune_against = init_stats([Ghost])
        self.immune_from = init_stats([Ghost])

class Fire(PokemonType):
    def __init__(self):
        super(Fire, self).__init__()
        self.strong_against = init_stats([Grass, Ice, Bug, Steel])
        self.weak_against = init_stats([Fire, Water, Rock, Dragon])
        self.vulnerable_to = init_stats([Water, Ground, Rock])
        self.resists = init_stats([Fire, Grass, Ice, Bug, Steel, Fairy])

class Water(PokemonType):
    def __init__(self):
        super(Water, self).__init__()
        self.strong_against = init_stats([Fire, Ground, Rock])
        self.weak_against = init_stats([Water, Grass, Dragon])
        self.vulnerable_to = init_stats([Grass, Electric])
        self.resists = init_stats([Fire, Water, Ice, Steel])

class Grass(PokemonType):
    def __init__(self):
        super(Grass, self).__init__()
        self.strong_against = init_stats([Water, Ground, Rock])
        self.weak_against = init_stats([Fire, Grass, Poison, Flying, Bug, Dragon, Steel])
        self.vulnerable_to = init_stats([Fire, Ice, Poison, Flying, Bug])
        self.resists = init_stats([Water, Grass, Electric, Ground])

class Electric(PokemonType):
    def __init__(self):
        super(Electric, self).__init__()
        self.strong_against = init_stats([Water, Flying])
        self.weak_against = init_stats([Grass, Electric, Dragon])
        self.vulnerable_to = init_stats([Ground])
        self.resists = init_stats([Electric, Flying, Steel])
        self.immune_against = init_stats([Ground])

class Ice(PokemonType):
    def __init__(self):
        super(Ice, self).__init__()
        self.strong_against = init_stats([Grass, Ground, Flying, Dragon])
        self.weak_against = init_stats([Fire, Water, Ice, Steel])
        self.vulnerable_to = init_stats([Fire, Fighting, Rock, Steel])
        self.resists = init_stats([Ice])

class Fighting(PokemonType):
    def __init__(self):
        super(Fighting, self).__init__()
        self.strong_against = init_stats([Normal, Ice, Rock, Dark, Steel])
        self.weak_against = init_stats([Poison, Flying, Psychic, Bug, Fairy])
        self.vulnerable_to = init_stats([Flying, Psychic, Fairy])
        self.resists = init_stats([Bug, Rock, Dark])
        self.immune_against = init_stats([Ghost])

class Poison(PokemonType):
    def __init__(self):
        super(Poison, self).__init__()
        self.strong_against = init_stats([Grass, Fairy])
        self.weak_against = init_stats([Poison, Ground, Rock, Ghost])
        self.vulnerable_to = init_stats([Ground, Psychic])
        self.resists = init_stats([Grass, Fighting, Poison, Bug, Fairy])
        self.immune_against = init_stats([Steel])

class Ground(PokemonType):
    def __init__(self):
        super(Ground, self).__init__()
        self.strong_against = init_stats([Fire, Electric, Poison, Rock, Steel])
        self.weak_against = init_stats([Grass, Bug])
        self.vulnerable_to = init_stats([Water, Grass, Ice])
        self.resists = init_stats([Poison, Rock])
        self.immune_against = init_stats([Flying])
        self.immune_from = init_stats([Electric])

class Flying(PokemonType):
    def __init__(self):
        super(Flying, self).__init__()
        self.strong_against = init_stats([Grass, Fighting, Bug])
        self.weak_against = init_stats([Electric, Rock, Steel])
        self.vulnerable_to = init_stats([Electric, Ice, Rock])
        self.resists = init_stats([Grass, Fighting, Bug])
        self.immune_from = init_stats([Ground])

class Psychic(PokemonType):
    def __init__(self):
        super(Psychic, self).__init__()
        self.strong_against = init_stats([Fighting, Poison])
        self.weak_against = init_stats([Psychic, Steel])
        self.vulnerable_to = init_stats([Bug, Ghost, Dark])
        self.resists = init_stats([Fighting, Psychic])
        self.immune_against = init_stats([Dark])

class Bug(PokemonType):
    def __init__(self):
        super(Bug, self).__init__()
        self.strong_against = init_stats([Grass, Psychic, Dark])
        self.weak_against = init_stats([Fire, Fighting, Poison, Flying, Ghost, Steel, Fairy])
        self.vulnerable_to = init_stats([Fire, Flying, Rock])
        self.resists = init_stats([Grass, Fighting, Ground])

class Rock(PokemonType):
    def __init__(self):
        super(Rock, self).__init__()
        self.strong_against = init_stats([Fire, Ice, Flying, Bug])
        self.weak_against = init_stats([Fighting, Ground, Steel])
        self.vulnerable_to = init_stats([Water, Grass, Fighting, Ground, Steel])
        self.resists = init_stats([Normal, Fire, Poison, Flying])

class Ghost(PokemonType):
    def __init__(self):
        super(Ghost, self).__init__()
        self.strong_against = init_stats([Psychic, Ghost])
        self.weak_against = init_stats([Dark])
        self.vulnerable_to = init_stats([Ghost, Dark])
        self.resists = init_stats([Poison, Bug])
        self.immune_against = init_stats([Normal])
        self.immune_from = init_stats([Normal, Fighting])

class Dragon(PokemonType):
    def __init__(self):
        super(Dragon, self).__init__()
        self.strong_against = init_stats([Dragon])
        self.weak_against = init_stats([Steel])
        self.vulnerable_to = init_stats([Ice, Dragon, Fairy])
        self.resists = init_stats([Fire, Water, Grass, Electric])
        self.immune_against = init_stats([Fairy])

class Dark(PokemonType):
    def __init__(self):
        super(Dark, self).__init__()
        self.strong_against = init_stats([Psychic, Ghost])
        self.weak_against = init_stats([Fighting, Dark, Fairy])
        self.vulnerable_to = init_stats([Fighting, Bug, Fairy])
        self.resists = init_stats([Ghost, Dark])
        self.immune_from = init_stats([Psychic])

class Steel(PokemonType):
    def __init__(self):
        super(Steel, self).__init__()
        self.strong_against = init_stats([Ice, Rock, Fairy])
        self.weak_against = init_stats([Fire, Water, Electric, Steel])
        self.vulnerable_to = init_stats([Fire, Fighting, Ground])
        self.resists = init_stats([Normal, Grass, Ice, Flying, Psychic, Bug, Rock, Dragon, Steel, Fairy])

class Fairy(PokemonType):
    def __init__(self):
        super(Fairy, self).__init__()
        self.strong_against = init_stats([Fighting, Dragon, Dark])
        self.weak_against = init_stats([Fire, Poison, Steel])
        self.vulnerable_to = init_stats([Poison, Steel])
        self.resists = init_stats([Fighting, Bug, Dark])
        self.immune_from = init_stats([Dragon])

def getattrs(obj):
    return [attr for attr in dir(obj) if not attr.startswith(("__","_")) and not type(getattr(obj, attr)) == types.MethodType]

def combine_stat(obj1, obj2, s1: str, s2: str):
    obj1_statA, obj1_statB = getattr(obj1, s1), getattr(obj1, s2)
    obj2_statA, obj2_statB = getattr(obj2, s1), getattr(obj2, s2)
    obj3_statA, obj3_statB = {}, {}
    if obj1_statA is not None:
        for stat in obj1_statA:
            if stat not in obj3_statA:
                obj3_statA[stat] = 1
            else:
                obj3_statA[stat] += 1
    if obj2_statA is not None:
        for stat in obj2_statA:
            if stat not in obj3_statA:
                obj3_statA[stat] = 1
            else:
                obj3_statA[stat] += 1
    if obj1_statB is not None:
        for stat in obj1_statB:
            if stat not in obj3_statB:
                obj3_statB[stat] = 1
            else:
                obj3_statB[stat] += 1
    if obj2_statB is not None:
        for stat in obj2_statB:
            if stat not in obj3_statB:
                obj3_statB[stat] = 1
            else:
                obj3_statB[stat] += 1
    if s1 == "strong_against" or s1 == "resists":
        for stat in obj3_statA:
            if stat in obj3_statB:
                obj3_statA[stat] -= 1
                obj3_statB[stat] -= 1

    for stat in obj3_statA.copy():
        if obj3_statA[stat] == 0:
            del(obj3_statA[stat]) # remove neutral stat
    for stat in obj3_statB.copy():
        if obj3_statB[stat] == 0:
            del(obj3_statB[stat]) # remove neutral stat

    return obj3_statA, obj3_statB

def handle_immune(pokemon):
    for immune in pokemon.immune_from:
        if immune in pokemon.vulnerable_to.copy():
            del(pokemon.vulnerable_to[immune])

def print_str_tuple(objs: tuple):
    if objs is not None:
        for obj in objs:
            print(obj.__name__,"",end="")
    print()

def print_str_dict(objs: dict):
    if objs is not None:
        for obj in objs:
            if(objs[obj] == 2):
                print(obj.__name__ + "(2x) ",end="")    
            else:
                print(obj.__name__,"",end="")
    print()

def init_stats(types):
    stat = {}
    for type in types:
        stat[type] = 1
    return stat
