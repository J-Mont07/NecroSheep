#section_one
import main_character as mc
#quick responses:
item = "The item was added to inventory"
reject = "Don't care for this item"
invalid = "Invalid input"
f = "Fausta"
n = "Narrator"
d = "YOU'RE DEAD"
e = "Press ENTER to Continue"
#Narrative:A little introduction of the story...

def start(player):
    print("On a stormy night... ",f," was inside his cell. Looking directly at the blank stone wall.")
    input(e)
    print (f," in his jail cell... with nothing but a limited ammount of food left.")
    input(e)
    print("He decides to look around his jail cell to find his escape")
    
#Interaction in this scene
    print("........................................................................")
    print ("As you observe the room... you noticed: ","\nbathroom","\nguard","\nbed")
    user_in = input(e)
    #ask user input for choosing what to do.
    while user_in.lower() != "bathroom" and user_in.lower() != "guard" and user_in.lower() != "bed":
##        print("Try Again")
        user_in = input("Choose where you would like to go: ")
        
        #Thus will execute if player chooses bathroom
        if user_in.lower() == "bathroom":
            print ("This Bathroom is dirty and it doesn't look like it works")
            user_in = input ("Choose where you would like to go: ")
        #This will execute if player chooses guard
        if user_in.lower() == "guard":
            print (f, ": That guard is sleeping... I think I can get its attention if I: ")
            print ("yell","\ncry","\nwall")
            action = input (e)
            while action.lower() != "yell" and action.lower() != "cry" and action.lower() != "wall":
                action = input ("Narrator: What do you think of doing: ")
            #Action within choosing guard
                if action.lower() == "yell":
                    print ("Narator:You got the guard's attention")
                    input(e)
                    print ("Narator:The guard is mad... He opens the cell and takes you to another room.")
                    input(e)
                    print ("...")
                    print ("Fausta: Where am I??")
                    input(e)
                    print("Fausta:Hmm...")
                    input(e)
                    print ("Fausta: It is full of wolves!!" + "\nAGHHHHHHHHHH!!!!")
                    input(e)
                    print ("Narator:Fausta has died...")
                    return d

                #This will excecute if player chooses cry within selecting guard.
                elif action.lower() == "cry":
                    print("Narrator: Nothing happens")
                    action = input ("Narrator: What do you think of doing: ")

                elif action.lower() == "wall":
                    print (f,"It appears that there is rocks on the floor")
                    input (e)
                    print (f,"I'm picking these up... might be useful for later")
                    input(e)
                    mc.main_character.pickup.append("rock")
                    print (item)
                    input(e)
                    print (f, "I could throw this to the guard!!")
                    mc.main_character.pickup.remove("rock")
                    print("Guard: HEYYYY!!!..." + "\n" + "Narator: The guard gets close to the cell")
                    input(e)
                    print ("Fausta: Look!!! He dropped his keys next to the cell!!!")
                    mc.main_character.pickup.append("key")
                    print(item)
                    input(e)
                    return

                #code couldn't be used
                #This will excecute if player chooses to throw a rock within selecting guard.
##                elif action.lower() == 'throw rock':
##                    mc.main_character.pickup.remove("rock")
##                    print("Fausta: Now let's throw this rock!!")
##                    input("")
##                    print("Guard: HEYYYY!!!..." + "\n" + "Narator: The guard gets close to the cell")
##                    print ("Fausta: Look!!! He dropped his keys next to the cell!!!")
##                    mc.main_character.pickup.append("key")
##                    print(item)
##                    return
        #This will execute if player chooses to go to bed.
        if user_in.lower() == "bed":
            print ("I can't sleep... I got to find a way out!!")
            user_in = input("Choose where you would like to go: ")

##        #This will excecute if player chosses wall.
##        if user_in == "wall":
##            print ("It appears that there is rocks on the floor")
##            print ("Fausta: Im picking these up... might be useful for later")
##            mc.main_character.pickup.append('rock')
##            print(item)
##            user_in = input ("choose where you would like to go: ")
            
##            pick_up = input ("Should I pick up the rocks? [Y/N]")
##            #if statement for picking up the item.
##            if pick_up.upper() == 'Y':
##                mc.main_character.pickup.append("rock")
##                print (item)
##            elif pick_up.upper() == 'N':
##                print (reject)
##            else:
##                print (reject)

##Code no being used:
##            if pick_up.upper() == "Y":
##                mc.pickup_items.append('rock')
##                print(item)
##            elif pick_up.upper() == "N":
##                print(reject)
##            else:
##                print(invalid)

## Notes:
#The player will proceed to secrtion 2 if they pass this part of the section.

#Requirements are find key, use pole to get keys, avoid gaurd.
#Go to section 3

#The player loses if he yells... The gaurd will take the player to another room.
