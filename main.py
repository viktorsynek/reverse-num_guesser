############################################   -== INFORMATION ==-   ############################################

#### THE PROGRAM WAS CREATED AND PUBLISHED BY:
#### https://github.com/viktorsynek
#### https://www.linkedin.com/in/viktor-synek/

#############################################   -== PROGRAM ==-   ###############################################

#IMPORT LIBRARIES
import time
from random import randint

def play_another():
    # IF USER INPUTS "N" THE PROGRAM STOPS
    print("Do you want to play another? (Y/N)")
    another = input(": ").lower()
    
    while another != "n" and another != "y":
        another = input(": ").lower()

    if another == "y":
        play() 

def play():
    try:
        lives = 3
        lst = []

        time.sleep(1)
        print("Think of a number, I'll try to guess it! (Between 0-15)")
        time.sleep(1)
        # USER THINKS OF THE NUMBER
        user = int(input("The number: "))

        while lives > 0:
            if user >= 0 and user <= 15:
                #BOT GUESS
                num = (randint(0,15))

                time.sleep(1)
            
                if num not in lst:
                    # BOT GUESSES A NUMBER, WHICH WE THEN PUT IN A LIST
                    print("Okay, let me see")
                    time.sleep(2)
                    print(f"What about {num}?")
                    lst.append(num)
                else:
                    # (#42) IF THE RANDOM NUMBER IS ALREADY IN THAT LIST, THE BOT INSTEAD GUESSES A DIFFERENT NUMBER
                    print("What about . . Hmm, nevermind. Lemme think of another one!")
                    continue

                if num == user:
                    time.sleep(1)
                    # BOT WINS
                    print("The bot guessed it! You lost. Better luck next time!")
                    time.sleep(1)
                    play_another()
                else:
                    time.sleep(1)
                    lives -= 1
                    # BOT INCORRECT GUESS
                    print(f"The bot did'nt guess it right, he has {lives} guess left")
                
                time.sleep(1)

            else:
                # USER DIDN'T GIVE THE NUMBER WITHIN THE GIVEN RANGE
                print("How about you giving me a number between 0-15? Wouldn't that be beautiful?")
                user = int(input("The number: "))

        time.sleep(1)
        # USER WINS
        print("The bot's life hit 0. You won the game. Congrats!")
        play_another()

    # HANDLE NOT NUMERIC INPUTS
    except ValueError:
        print("That's not a number!")
        play() 
        

play()
