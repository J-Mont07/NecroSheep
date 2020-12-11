import random

class mobs:
    hp = 0
    name = ""
    attack = 0

    def __init__ (self, name, hp, attack):
        self.hp = hp
        self.name = name
        self.attack = attack
class boss:
    hp = 0
    name = ""
    attack = random.randint(4,8)

    def __init__ (self, name, hp):
        self.hp = hp
        self.name = name
