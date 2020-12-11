#Section 2
import main_character as mc

#Quck responses:
con = "Let us continue"
e = "Press ENTER to continue"
n = "Narrator:"
f = "Fausta"
d = "YOU'RE DEAD"
#Narrative in continuation to the story...
#Start chapter 2.
def start (player):
    print (n,"Fausta has collected the key!!" + "\n",n,"Now it's your chance to make a run for it!")
    input (e)
    print ("...Distant yelling...")
    input (e)
    print (f, "Why is there alot of noise coming from the outside?" + " That doesn't consern me... Lets get out of here.")
    #While loop so the player can make choices.
    open_cell = input (e)
    while open_cell.upper() != "N" and open_cell.upper() != "Y":
        open_cell = input("Fausta: Shall we open the cell? [Y/N]: ")
        if open_cell.upper() == "Y":
            print (con)
        elif open_cell.upper() == "N":
            print ("Fausta: I don't care what you say... IM LEAVING!")

    print ("Narrator: As Fausta exits the cell he looks around.")
    input(e)
    print ("Narrator: As you observe the room you notice:" + "\nbody" +"\ntable" + "\nchest" + "\nlocker" + "\nexit")
    user_in = input (e)

    while user_in.lower() != "body" and user_in.lower() != "table" and user_in.lower() != "chest" and user_in.lower() != "locker" and user_in.lower() != "exit":
        user_in = input("Narrator: What would you like to do?")
        #If user choses body this will excecutre
        if user_in.lower() == "body":
            print ("YUCK" + "\nThis body smells bad")
            input (e)
            print ("Theres a piece of paper!")
            action_grab = input ("Should I pick it up? [Y/N]")
            if action_grab.upper() == "Y":
                print ("Hmmmm..." "\nWeird is is just numbers... 1216")
            elif action_grab.upper() == "N":
                print ("Let's keep on moving")
            else:
                print ("Don't care about it")    
            user_in = input("Narrator: What would you like to do?")
        #If user chooses table this will excecute
        if user_in.lower() == "table":
            print("Fausta: OHHH there's some food in the table!")
            action_pick = input ("I'm hungry... should I eat it? [Y/N]: ")
            if action_pick.upper() == "Y":
                print ("Fausta: Yum, but it tasted a bit weird..." +"\nI feel more energized!")
                print ("*BOOOOMMMM*", "\n....")
                input (e)
                print ("Narator: Fausta died")
                return
            elif action_pick.upper() == "N":
                print ("Fausta: I wasn't hungry anyways...")
            else:
                print ("Fausta: I wasn't hungry anyways...")
            user_in = input("Narrator: What would you like to do?")
        #If user chooses chest this will excecute
        if user_in.lower() == "chest":
            print("Fausta: OHHHHH....shinny gold chest!")
            print("Narrator: As you open the chest you find a shield.")
            mc.main_character.pickup.append("shield")
            user_in = input ("Narrator: What would you like to do?: ")
        #if user chooses locker this will excecute
        if user_in.lower() == "locker":
            print ("Fausta: HMMM... It says ENTER PASSCODE: ")
            print ('Fausta: I can either "exit" or attempt to enter a passcode.')
            put_password = input(e)
            while put_password.lower() != "1216" and put_password.lower() != "exit":
                #Keeps printing enter password
                put_password = input("EXIT or ","ENTER PASSCODE: ")
                if put_password == "1216":
                    print ("ACCESS GRANTED")
                    print ("Fausta: AWESOME a long great sword!")
                    mc.main_character.pickup.append("great sword")
                    break
                elif put_password.lower() == "exit":
                    break
            user_in = input ("Narraror: What would you like to do?: ")
        #User will be able to exit the level
        if user_in.lower() == "exit":
            print ("Lets get out of here!!!")
            return
            
#Interaction in this scene:
#Open cell
#Pick up shield
#Examine body
#Eat food
#Search chest
#Examine locker

#Requirements is player must open cell. And leave the room.

#Optional: pick up shield

#Bonus items: silver great sword (deals 4 damage.
