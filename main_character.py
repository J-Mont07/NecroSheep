#Fausta
#Grey mature sheep.
#Weights 250 pounds.
#Master of using a great sword and a master in dexterity.
import random

class main_character:
    a = 0
    hp = 20
    #starting items
    inventory = [a,hp]

    #append items here
    pickup = []
    items = []

    #def use_item()

#function to call attack...
    def attack():
        x = 0
        for x in range(len(main_character.pickup)):
            if main_character.pickup[x] == "silver sword":
                x = x + 1
                return random.randint(5,8)
        else:
            return random.randint(2,3)
#Function for player to heal themself on combat
    def heal():
        while main_character.hp >= 1 and main_character.hp <=20:
            x = 0
            y = 0
            for x in range(len(main_character.items)):
                if main_character.items[x] == "health_potion":
                    health_potion = 5
                    main_character.hp = main_character.hp + health_potion
                    return main_character.hp
            else:
                print("You do not have any health potions")
                return main_character.hp
            
#Function that adds armor top 
    #def arm():
