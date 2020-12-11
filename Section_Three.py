#Section 3
import main_character as mc
import combat as c 
import enemies as e
import mob as m

#Quick responses
e = "Press ENTER to continue"
f = "Fausta:"
n = "Narrator:"
w = "you have won the battle"

#Narrative: The continution form section 2.
def start (player):
    print ("Narrator: As Fausta come out of the room. He notices that it's to quiet...")
    input (e)
    print ("Fausta: It's really quiet, it creeps me out... must have my guard up!")
    input (e)
    print ("...", "\nFausta:AHHHHHHHHHHH......")

    print ("Narrator: You have fallen down a trap door...")
    print ("Narrator: You'll have to find your way out of this place...")
    input(e)
    #Interaction in this level:
    print ("You're able to move: " ,"\nstraight","\nleft","\nright")
    choose_opt = input (e)
    while choose_opt.lower() != "straight" and choose_opt.lower() != "left" and choose_opt.lower() != "right":
        choose_opt = input ("Select where you would like to move: ")
        #Desicions player will make
        if choose_opt.lower() == "left":
            #Starts fight with rat enemy
##            print (c.rat())
            rat = m.mobs("Rat", 4, 3)
##            print (rat.name, rat.hp, rat.attack)
            #Starts combat module
            print (c.combat(rat.name, rat.hp, rat.attack))
            #Checks is player is alive or dead
            if mc.main_character.hp <=0:
                print("YOU'RE DEAD")
                return
            #Continues if alive
            print (n,w)
            input (e)
            print(f,"OHH!! A DOOR!")
            print(n,"As you open the door...")
            print (f"AGHHHHHH....")
            print("...")
            print ("Narrator: you have been impaled by spikes.")
            print ("YOU'RE DEAD")
            return

        elif choose_opt.lower() == "right":
            print ("Narrator: Looked like you fell in a pit of lava!")
            print ("YOU'RE DEAD")
            return
        
        #This will be the process the player has to make in order to complete the level
        elif choose_opt.lower() == "straight":
        #The player will have to fight an enemey first to continue
            goblin = m.goblin("Goblin",8 ,4)
            #Starts combat module 
            print (c.combat(goblin.name, goblin.hp, goblin.attack))
            #Checks if player is alive or dead when it returns
             if mc.main_character.hp <=0:
                print("YOU'RE DEAD")
                return
            #Continues if alive
            print (w)
            print("Theres still more exits to choose from.")
            print ("Select where you would like to move: " ,"\nstraight","\nleft","\nright")
            second_opt = input(e)
        
        while second_opt.lower() != "straight" and second_opt.lower() != "\nleft" and second_opt.lower() != "\nright":
            second_opt = input("Select where you would like to move: ", "\nstraight","\nleft","\nright")
            if second_opt.lower() == "straight":
                print (f,"AHHHHHHHH")
                input(e)
                print(n, "You have fallen into a pit of spikes!!")
                return
            elif second_opt.lower() == "right":
                #Another fight will begin
                print ("Fausta: It still looks the same to me... I'm going the right way... I think")
                third_opt = input(e)
                while third_opt.lower() != "straight" and third_opt.lower() != "\nleft" and third_opt.lower() != "\nright":
                    third_opt = input("Select where would you like to move: ")
                    if third_opt == "straight":
                        #A fight will begin
                        print (f,"There seems to be a door! I found the EXIT!!!")
                        return
                    elif third_opt.lower() == "left":
                        print ("*DISTANT SHOOTING*")
                        print (n,"YOU'RE DEAD")
                        return
                    
                    elif third_opt.lower() == "right":
                        print ("*DISTSTANT RUMBBLE*")
                        print (n,"You have been crushed by a boulder")
                        return
            elif second_opt.lower() == "left":
                print (f, "A weird looking door!!!")
                print (f, "Got no other option to go in")
                print ("*EXPLOSION*")
                print (n,"YOU'RE DEAD")
                return

#Fight
#Escape

#The player will be reqiured to find there way out in this maze.
#Consiststs of mobs:
#Goblins
#Rats
#knights

#Player must find the exit. And beat the mini boss. There will bed dead ends.

#Go to section 4

#Player will lose if he dies. or falls in the trap doors.
