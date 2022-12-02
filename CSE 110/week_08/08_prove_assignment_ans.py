# ---------------------------------------------------------------------------- #
#                                    imports                                   #
# ---------------------------------------------------------------------------- #
from random_word import RandomWords # imports random word module

# ---------------------------------------------------------------------------- #
#                                   main body                                  #
# ---------------------------------------------------------------------------- #
playing = True # boolean for while loop

print("Welcome to the Word Guessing Game!\n") # entrance message

while playing: # loops while the player wants to play
    secret =  RandomWords().get_random_word()# secret word
    unsolved = True # boolean for while loop
    hint = "Your hint is: " # hint text
    attempts = 0 # tracks number of attempts

    print("Your hint is: " + "_ " * len(secret)) # prints hint

    while unsolved: # loops while the puzzle is not solved
        guess = input("What is your guess? ").lower() # get user input for guess
        attempts += 1 # adds to the attempts count

        if guess == secret: # if player guesses the secret word
            unsolved = False # stop the loop

            if attempts == 1: # if first try
                print("Congratulations! You guessed it on your first try! Are you sure you aren't cheating?") # accuse cheating

            else: # if more than one try
                print(f"Congratulations! You guessed it in {attempts} tries!") # congratulate player

            again = input("Do you want to play again? (y/n) ").lower() # ask if player wants to play again


            if again == 'y': # if player answers y
                playing = True # keep playing

            else: # if player answers anything else
                print("Thanks for playing! ") # thank player
                playing = False # break playing loop to end game

        elif len(secret) == len(guess): # if guess is not correct and same length as the secret word
            
            for i in range(len(secret)): # gets the length of the secret word to loop through each letter individually
                validLetter = False # boolean for printing

                if secret[i] == guess[i]: # checks if the letter is in the correct spot
                    hint += guess[i].upper() + " " # adds the guess letter to the hint
                    validLetter = True # valid letter
                
                else: # checks if the letter is in the word
                    for letter in secret: # checks each letter in the secret word
                        if guess[i] == letter: # if the letter from the secret word matches the guessed letter
                            hint += guess[i] + " " # adds the guess to the hint lowercase
                            validLetter = True  # valid letter
                            break

                    if not validLetter: # if none of the other if statements are true
                        hint += "_ " # add a blank underscore

            print(hint) # print out the hint

            hint = "Your hint is: " # blank the hint

        else: # if the guess is not the same length as the secret word
            print("Incorrect number of characters in guess.") # humiliate player