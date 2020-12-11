#Remember to put all your files into the same folder on your computer!
#Otherwise, these import statements won't be able to find them properly

e = "Press ENTER to continue"
#Import all files you'll need to run this properly
import main_character as mc
import Section_one as sec_one
import Section_Two as sec_two
import Section_Three as sec_three


#Create our player character from our main_character class
death_count = 0
player = mc.main_character()

#Intro text to the user
#The empty input functions are only here so the player has to type something to move on
#(like pressing a button in a video game to move the dialogue along)
##print("WELCOME TO NECROSHEEP!")
##input (e)
##user = input("Are you ready for this challenge? [Y/N]" +"\n")
##
##while user.upper() != 'Y' and user.upper() != 'N':
##    print ("Try again...")
##    user = input ("Are you ready for this challange? [Y/N]" + "\n")
##if user.upper() == "Y":
##    print ("Let the game begin")
##    sec_one.start(player)
##
##elif user.upper() == "N":
##    print ("HAHAHA I knew you weren't up for the challange" )
##
###once the player finishes the first level the second level will execute.
##
###This code will run chapter two
##print("You have completed the first challance.")
##input (e)
##print("Lets continue your Journey...")
##sec_two.start(player)

#This code will run chapter three
print("Amazing!! This journy hasn't been that dificult for you.")
input(e)
print ("Keep up that great work!")
sec_three.start(player)

#if user.upper() == "Y":
#    print ("Let the game begin")
#    Section_one.start(player)
#elif user.upper() == "N":
#    print ("HAHAHA I knew you weren't up for the challange")
#else:
#    print ("Try again...")
    
#And do/say anything else to get your game started

#Then call your first section.
#Be sure to pass in your player character
