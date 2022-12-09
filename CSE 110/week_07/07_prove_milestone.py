# Made by Brady Hodge
# CSE 110
# 07 Prove: Assignment Milestone - Wordle

"""
+ added a limit to the number of guesses the user can make for the stretch goal
"""

# welcome the user
print("Welcome to the word guessing game!")

# define variables
magic_word = "broken"
user_guess = ""
guess_count = 0

# loop the guessing until the user guess the word or run out of guesses
while user_guess != magic_word and guess_count < 6:
    user_guess = input("What is your guess? ")
    guess_count += 1
    if user_guess != magic_word:
        print("Your guess was not correct.")
        print(f"Guess {guess_count}/6")

# print the result
if user_guess == magic_word:
    print("Congratulations! You guessed the word!")
    print(f"It took you {guess_count} guesses.")
else:
    print("You have run out of guesses. Better luck next time!")
    print(f"The word was {magic_word}.")
