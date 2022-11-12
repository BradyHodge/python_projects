# --------------------
# Made by Brady Hodge
# Status: Graded
# Lab 7a pt 1 of 1
# --------------------

import random


def get_game_limit(lower, upper):
    try_again = True

    while try_again == True:
        game_limit = int(input("Pick a number between {} and {}. ".format(lower, upper)))
        if lower <= game_limit <= upper:
            return game_limit
            print(game_limit, "will be the upper limit, so be careful not to go over.")
            try_again = False
        else:
            print("Invalid input, please try again.")
            try_again = True


def do_we_roll():
    try_again = True

    while try_again == True:
        roll_again = str(input("Would you like to roll the dice(yes/no)? "))
        if roll_again == "yes":
            return True
            try_again = False
        elif roll_again == "no":
            return False
            try_again = False
        else:
            print("Invalid input, please try again.")
            try_again = True


game_limit = get_game_limit(7, 25)
total_roll = 0
keep_playing = True

while keep_playing == True and total_roll < game_limit:
    keep_playing = do_we_roll()
    if keep_playing == True:
        print("Rolling the dice...")
        current_roll = random.randrange(1, 7)
        print("You rolled", current_roll)
        total_roll = total_roll + current_roll
        print("Your total is", total_roll)

print("----------")
if total_roll < game_limit:
    print("You were", game_limit - total_roll, "under the limit!")
if total_roll > game_limit:
    print("Sorry, you went", total_roll - game_limit, "over the limit. Better luck next time.")
if total_roll == game_limit:
    print("You matched the limit! You couldn't have done better, literally.")
