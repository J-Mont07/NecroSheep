#combat section
import main_character as mc
import enemies as e
import random

#quick responses:
f = "Fausta:"
n = "Narrator:"
d = "YOU ARE'DEAD"
s = "You have slayed the enemy!!"
m = "Press ENTER to continue"
b = "You took no damage"
h = "HP remaining"


## call it when using rat
##combat(e.rat.name, e.rat.hp, e.rat.attack)

## call it when using goblin

##combat.combat(e.goblin.name, e.goblin.hp, e.goblin.attack)

def combat(name, hp, attack):
    print(f,"Looks like we are fighting a",name)
    print (f,"Looks weak, it has",hp,"HP")
    print("....................................")
    print("Let the fighitng BEGIN")
    print ("You got to choose between two actions: ", "\nattack","\nblock")
    choose = input(m)
    while mc.main_character.hp >= 0:
        choose = input("What do you want to do?")
        if choose.lower() == "attack":
            hp = hp - mc.main_character.attack()
            print("Nice hit!!", name,"HP left:",hp)
            if hp <= 0:
                print(s)
                print(h)
                return mc.main_character.hp
            print("Now its",name,"turn")
            mc.main_character.hp = mc.main_character.hp - attack
            print("you got hit","HP left:",mc.main_character.hp)
        if choose.lower() == "block":
            print(b)
            print("HP left:",mc.main_character.hp)
            #Checks inventory
        if choose.lower() == "inventory":
            x = 0
            for x in range(len(mc.main_character.items)):
                print ("Here is what you have so far")
                print (mc.main_character.items[x])
            #Player is able to heal
        if choose.lower() == "heal":
            mc.main_character.heal()
            print("HP:",mc.main_character.hp)

    else:
        return mc.main_character.hp

#OLD FUNCTIONS
##def rat():
##    print(f,"Looks like we are fighting a",e.rat.name)
##    print (f,"Looks weak, it has",e.rat.hp,"HP")
##    print("....................................")
##    print("Let the fighitng BEGIN")
##    print ("You got to choose between two actions: ", "\nattack","\nblock")
##    choose = input(m)
##    while mc.main_character.hp >= 0:
##        choose = input("What do you want to do?")
##        if choose.lower() == "attack":
##            e.rat.hp = e.rat.hp - mc.main_character.attack()
##            print("Nice hit!!", e.rat.name,"HP left:",e.rat.hp)
##            if e.rat.hp <= 0:
##                print(s)
##                print(h)
##                return mc.main_character.hp
##            print("Now its",e.rat.name,"turn")
##            mc.main_character.hp = mc.main_character.hp - e.rat.attack
##            print("you got hit","HP left:",mc.main_character.hp)
##        if choose.lower() == "block":
##            print(b)
##            print("HP left:",mc.main_character.hp)
##            #Checks inventory
##        if choose.lower() == "inventory":
##            x = 0
##            for x in range(len(mc.main_character.items)):
##                print ("Here is what you have so far")
##                print (mc.main_character.items[x])
##            #Player is able to heal
##        if choose.lower() == "heal":
##            mc.main_character.heal()
##            print("HP:",mc.main_character.hp)
##
##    else:
##        return mc.main_character.hp
##
##            
##def goblin():
##    print(f, "Looks like we are fighting a",e.goblin.name)
##    print(f, "It has",e.goblin.hp,"HP")
##    print("....................................")
##    print("Let the fighitng BEGIN")
##    print ("You got to choose between two actions: ", "\nattack","\nblock")
##    choose = input(m)
##    while mc.main_character.hp >= 0:
##        choose = input("What do you want to do?")
##        if choose.lower() == "attack":
##            e.goblin.hp = e.goblin.hp - mc.main_character.attack()
##            print("Nice Hit!!", e.goblin.name, "HP left:",e.rat.hp)
##            if e.goblin.hp <=0:
##                print(s)
##                print(h)
##                return mc.main_character.hp
##            print ("Now its", e.goblin.name,"turn")
##            mc.main_character.hp = mc.main_character.hp - e.goblin.attack
##            print("You got hit","HP left:",mc.main_character.hp)
##        if choose.lower() == "block":
##            print(b)
##            print("HP left:",mc.main_character.hp)
##            #Checks inventory
##        if choose.lower() == "inventory":
##            x = 0
##            for x in range(len(mc.main_character.items)):
##                print ("Here is what you have so far")
##                print (mc.main_character.items[x])
##            #Player is able to heal
##        if choose.lower() == "heal":
##            mc.main_character.heal()
##            print("HP:",mc.main_character.hp)
##    else:
##        return mc.main_character.hp
    
