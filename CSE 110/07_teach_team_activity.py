# Made by Brady Hodge
# CSE 110
# 07 Teach: Team Activity - Guess My Number Game

# import modules 
import random

# loop the game
keep_going = "yes"

while keep_going == "yes":

    # generate a random number
    magic_numb = random.randint(1, 100)
    guess_numb = int(input("What is your guess? "))
    guess_count = 1

    # loop the guessing
    while magic_numb != guess_numb:
        if magic_numb > guess_numb:
            print("Higher")
        
        elif magic_numb < guess_numb:
            print("Lower")

        else: 
            print("You guessed it!")

        guess_numb = int(input("What is your guess? "))
        guess_count += 1
    print(f"It took you {guess_count} guesses")
    keep_going = input("Would you like to play again (yes/no)? ")