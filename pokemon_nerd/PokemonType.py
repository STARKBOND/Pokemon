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
        self.type = type(self)
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
        for attr in self.attrs:
            if getattr(self, attr) == None:
                self.attrs.remove(attr)
            match(attr):
                case "type":
                    print("Type: {}".format(self.type))
                case "strong_against":
                    print("Strong against: {}".format(self.strong_against))
                case "weak_against":
                    print("Weak against: {}".format(self.weak_against))
                case "vulnerable_to":
                    print("Vulnerable to: {}".format(self.vulnerable_to))
                case "resists":
                    print("Resists: {}".format(self.resists))
                case "immune_from":
                    print("Immune from: {}".format(self.immune_from))
                case "immune_against":
                    print("Doesn't affect: {}".format(self.immune_against))
                case _:
                    pass
class DualType(PokemonType):
    def __init__(self, poke_t1: PokemonType, poke_t2: PokemonType):
        super(DualType, self).__init__()
        self.type = poke_t1, poke_t2

class Normal(PokemonType):
    def __init__(self):
        super(Normal, self).__init__()
        self.weak_against = [Rock, Steel]
        self.vulnerable_to = [Fighting]
        self.immune_against = [Ghost]
        self.immune_from = [Ghost]

class Fire(PokemonType):
    def __init__(self):
        super(Fire, self).__init__()
        self.strong_against = [Grass, Ice, Bug, Steel]
        self.weak_against = [Fire, Water, Rock, Dragon]
        self.vulnerable_to = [Water, Ground, Rock]
        self.resists = [Fire, Grass, Ice, Bug, Steel, Fairy]

class Water(PokemonType):
    def __init__(self):
        super(Water, self).__init__()
        self.strong_against = [Fire, Ground, Rock]
        self.weak_against = [Water, Grass, Dragon]
        self.vulnerable_to = [Grass, Electric]
        self.resists = [Fire, Water, Ice, Steel]

class Grass(PokemonType):
    def __init__(self):
        super(Grass, self).__init__()
        self.strong_against = [Water, Ground, Rock]
        self.weak_against = [Fire, Grass, Poison, Flying, Bug, Dragon, Steel]
        self.vulnerable_to = [Fire, Ice, Poison, Flying, Bug]
        self.resists = [Water, Grass, Electric, Ground]

class Electric(PokemonType):
    def __init__(self):
        super(Electric, self).__init__()
        self.strong_against = [Water, Flying]
        self.weak_against = [Grass, Electric, Dragon]
        self.vulnerable_to = [Ground]
        self.resists = [Electric, Flying, Steel]
        self.immune_against = [Ground]

class Ice(PokemonType):
    def __init__(self):
        super(Ice, self).__init__()
        self.strong_against = [Grass, Ground, Flying, Dragon]
        self.weak_against = [Fire, Water, Ice, Steel]
        self.vulnerable_to = [Fire, Fighting, Rock, Steel]
        self.resists = [Ice]

class Fighting(PokemonType):
    def __init__(self):
        super(Fighting, self).__init__()
        self.strong_against = [Normal, Ice, Rock, Dark, Steel]
        self.weak_against = [Poison, Flying, Psychic, Bug, Fairy]
        self.vulnerable_to = [Flying, Psychic, Fairy]
        self.resists = [Bug, Rock, Dark]
        self.immune_against = [Ghost]

class Poison(PokemonType):
    def __init__(self):
        super(Poison, self).__init__()
        self.strong_against = [Grass, Fairy]
        self.weak_against = [Poison, Ground, Rock, Ghost]
        self.vulnerable_to = [Ground, Psychic]
        self.resists = [Grass, Fighting, Poison, Bug, Fairy]
        self.immune_against = [Steel]

class Ground(PokemonType):
    def __init__(self):
        super(Ground, self).__init__()
        self.strong_against = [Fire, Electric, Poison, Rock, Steel]
        self.weak_against = [Grass, Bug]
        self.vulnerable_to = [Water, Grass, Ice]
        self.resists = [Poison, Rock]
        self.immune_against = [Flying]
        self.immune_from = [Electric]

class Flying(PokemonType):
    def __init__(self):
        super(Flying, self).__init__()
        self.strong_against = [Grass, Fighting, Bug]
        self.weak_against = [Electric, Rock, Steel]
        self.vulnerable_to = [Electric, Ice, Rock]
        self.resists = [Grass, Fighting, Bug]
        self.immune_from = [Ground]

class Psychic(PokemonType):
    def __init__(self):
        super(Psychic, self).__init__()
        self.strong_against = [Fighting, Poison]
        self.weak_against = [Psychic, Steel]
        self.vulnerable_to = [Bug, Ghost, Dark]
        self.resists = [Fighting, Psychic]
        self.immune_against = [Dark]

class Bug(PokemonType):
    def __init__(self):
        super(Bug, self).__init__()
        self.strong_against = [Grass, Psychic, Dark]
        self.weak_against = [Fire, Fighting, Poison, Flying, Ghost, Steel, Fairy]
        self.vulnerable_to = [Fire, Flying, Rock]
        self.resists = [Grass, Fighting, Ground]

class Rock(PokemonType):
    def __init__(self):
        super(Rock, self).__init__()
        self.strong_against = [Fire, Ice, Flying, Bug]
        self.weak_against = [Fighting, Ground, Steel]
        self.vulnerable_to = [Water, Grass, Fighting, Ground, Steel]
        self.resists = [Normal, Fire, Poison, Flying]

class Ghost(PokemonType):
    def __init__(self):
        super(Ghost, self).__init__()
        self.strong_against = [Psychic, Ghost]
        self.weak_against = [Dark]
        self.vulnerable_to = [Ghost, Dark]
        self.resists = [Poison, Bug]
        self.immune_against = [Normal]
        self.immune_from = [Normal, Fighting]

class Dragon(PokemonType):
    def __init__(self):
        super(Dragon, self).__init__()
        self.strong_against = [Dragon]
        self.weak_against = [Steel]
        self.vulnerable_to = [Ice, Dragon, Fairy]
        self.resists = [Fire, Water, Grass, Electric]
        self.immune_against = [Fairy]

class Dark(PokemonType):
    def __init__(self):
        super(Dark, self).__init__()
        self.strong_against = [Psychic, Ghost]
        self.weak_against = [Fighting, Dark, Fairy]
        self.vulnerable_to = [Fighting, Bug, Fairy]
        self.resists = [Ghost, Dark]
        self.immune_from = [Psychic]

class Steel(PokemonType):
    def __init__(self):
        super(Steel, self).__init__()
        self.strong_against = [Ice, Rock, Fairy]
        self.weak_against = [Fire, Water, Electric, Steel]
        self.vulnerable_to = [Fire, Fighting, Ground]
        self.resists = [Normal, Grass, Ice, Flying, Psychic, Bug, Rock, Dragon, Steel, Fairy]

class Fairy(PokemonType):
    def __init__(self):
        super(Fairy, self).__init__()
        self.strong_against = [Fighting, Dragon, Dark]
        self.weak_against = [Fire, Poison, Steel]
        self.vulnerable_to = [Poison, Steel]
        self.resists = [Fighting, Bug, Dark]
        self.immune_from = [Dragon]

def getattrs(obj):
    return [attr for attr in dir(obj) if not attr.startswith(("__","_")) and not type(getattr(obj, attr)) == types.MethodType]

def combine_stat(poke_t1, poke_t2, s1: str, s2: str):
    poke_t1_statA, poke_t1_statB = getattr(poke_t1, s1), getattr(poke_t1, s2)
    poke_t2_statA, poke_t2_statB = getattr(poke_t2, s1), getattr(poke_t2, s2)
    dual_type_statA, dual_type_statB = [], []
    if poke_t1_statA is not None:
        for stat in poke_t1_statA:
            dual_type_statA.append(stat)
    if poke_t2_statA is not None:
        for stat in poke_t2_statA:
            dual_type_statA.append(stat)
    if poke_t1_statB is not None:
        for stat in poke_t1_statB:
            dual_type_statB.append(stat)
    if poke_t2_statB is not None:
        for stat in poke_t2_statB:
            dual_type_statB.append(stat)
    if s1 == "strong_against" or s1 == "resists":
        statA = [stat for stat in dual_type_statA if stat not in dual_type_statB]
        statB = [stat for stat in dual_type_statB if stat not in dual_type_statA]
    elif s1 == "immune_against":
        statA = [stat for stat in dual_type_statA]
        statB = [stat for stat in dual_type_statB]

    return statA, statB

def handle_immune(pokemon):
    pass
    for i in pokemon.immune_from:
        if i in pokemon.vulnerable_to:
            pokemon.vulnerable_to.remove(i)

