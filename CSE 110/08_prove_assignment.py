# Made by Brady Hodge
# CSE 110
# 08 Prove: Assignment - Wordle

"""
+ added 6 guess limit to increase difficulty for stretch goal
+ added wordlist and random.choice to pick a random answer for stretch goal
"""

# import modules
import random

# welcome the user
print("Welcome to the word guessing game!")

# define variables
wordlist = ["number", "people", "little", "differ", "before", "follow", "change", "animal", "mother", "father", "should", "answer", "school", "always", "letter", "second", "friend", "enough", "though", "family", "direct", "happen", "better", "during", "ground", "listen", "travel", "simple", "toward", "center", "person", "appear", "govern", "notice", "figure", "beauty", "minute", "strong", "behind", "street", "course", "object", "decide", "island", "system", "record", "common", "wonder", "equate", "engine", "settle", "weight", "matter", "circle", "divide", "sudden", "square", "reason", "length", "region", "energy", "forest", "window", "summer", "winter", "bright", "finish", "flower", "clothe", "either", "result", "phrase", "silent","finger", "excite", "middle", "moment", "spring", "nation", "method", "design", "bottom", "single", "twenty", "crease", "melody", "office", "symbol", "except", "garden", "choose", "gentle", "doctor", "please", "locate", "insect", "caught", "period", "effect", "expect", "modern", "corner", "supply", "danger", "create", "rather", "string", "depend", "famous", "dollar", "stream", "planet", "colony", "search", "yellow", "desert", "spread", "invent", "cotton", "chance", "gather", "column", "select", "repeat", "plural", "oxygen", "pretty", "season", "magnet", "silver", "branch", "suffix", "afraid", "sister", "bought", "valley", "double", "arrive", "master", "parent", "charge", "proper", "market", "degree", "speech", "nature", "motion", "liquid"]
magic_word = random.choice(wordlist)
user_guess = ""
guess_count = 0

# give the user a blank hint for the start of the game
for letter in range(len(magic_word)):
    user_guess += "_"

# loop the guessing until the user guess the word or run out of guesses
while user_guess != magic_word and guess_count < 6:
    print("Your hint is: ", end="")
    # find if each letter is in magic_word
    for i in range(len(magic_word)):
        contains_char = False
        if magic_word[i] == user_guess[i]:
            print(user_guess[i].upper(), end=" ")
            contains_char = True
        else:
            for letter in magic_word:
                if user_guess[i] == letter:
                    print(user_guess[i], end=" ")
                    contains_char = True
                    break
            if not contains_char:
                print("_", end=" ")
    # get the user guess
    user_guess = input("\nWhat is your guess? ").lower()
    if len(user_guess) == len(magic_word):
        guess_count += 1
        if user_guess != magic_word:
            print("Your guess was not correct.")
            print(f"Guess {guess_count}/6")
    # if user_guess does not have the correct number of letters tell the user
    else:
        print("Sorry, the guess must have the same number of letters as the secret word.")
        # reset user guess
        user_guess = ""
        for x in range(len(magic_word)):
            user_guess += "_"

# print the result
if user_guess == magic_word:
    print("Congratulations! You guessed the word!")
    print(f"It took you {guess_count} guesses.")
else:
    print("You have run out of guesses. Better luck next time!")
    print(f"The word was {magic_word}.")
