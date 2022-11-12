import random


def get_game_limit(min_val: int, max_val: int) -> int:
    """Get the maximum score from the user, it needs to fall between the minimum and the maximum"""
    number_valid = False
    while not number_valid:
        number_str = input("What will be the goal?\nPick a number between " +
                           str(min_val) + "and" + str(max_val) + ": ")
        number = int(number_str)
        if number >= min_val and number <= max_val:
            number_valid = True
        else:
            print("I am sorry, that was not a valid number.")
            number = -1
        return number


def do_we_roll() -> bool:
    """Ask the user if they roll again. Return true if they wish to continue, false if no.
    keep asking otherwise."""
    ask_again = True
    while ask_again:
        user_answer = input("Do you want to roll the die (yes|no)? ")
        ask_again = False
        if user_answer == "Yes" or user_answer == "yes" or user_answer == "y":
            go_on = True

        elif user_answer == "No" or user_answer == "no" or user_answer == "n":
            go_on = False
        else:
            print("I did not understand.")
            ask_again = True
    return go_on

# get game goal
game_goal = get_game_limit(7, 25)
game_score = 0
play_game = game_score < game_goal

# print instructions
print()
print("Reach " + str(game_goal) + """without going over.
You can stop at any time.
See how close you can get?\n""")

# play the game

# game over; display results

# roll dice while less that a given number, if next roll exceeds number,
#stop rolling. Count the number of rolls.
