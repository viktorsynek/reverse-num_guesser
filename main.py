# REVERSE GUESS THE NUMBER BETWEEN 0-15
# THE USER SETS THE NUMBER AND THE PROGRAM TRIES TO FIGURE IT OUT
# IF THE PROGRAM GUESS IT IN LESS THAN 3 MOVES, THEN IT WINS OTHERWISE, THE USER WINS

import time
from random import randint

def play_another():
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
        user = int(input("The number: "))

        while lives > 0:
            if user >= 0 and user <= 15:
                
                num = (randint(0,15))

                time.sleep(1)
            
                if num not in lst:
                    print("Okay, let me see")
                    time.sleep(2)
                    print(f"What about {num}?")
                    lst.append(num)
                else:
                    print("What about . . Hmm, nevermind. Lemme think of another one!")
                    continue

                if num == user:
                    time.sleep(1)
                    print("The bot guessed it! You lost. Better luck next time!")
                    time.sleep(1)
                    play_another()
                else:
                    time.sleep(1)
                    lives -= 1
                    print(f"The bot did'nt guess it right, he has {lives} guess left")
                
                time.sleep(1)

            else:
                print("How about you giving me a number between 0-15? Wouldn't it be beautiful?")
                user = int(input("The number: "))

        time.sleep(1)
        print("The bot's life hit 0. You won the game. Congrats!")
        play_another()

    except ValueError:
        print("That's not a number!")
        play()
        

play()
