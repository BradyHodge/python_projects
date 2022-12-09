# --------------------
# Made by Brady Hodge
# Status: Done
# Lab 6C pt 2 of 2
# --------------------

import random
import date_parts

# ask user to pick first date part: travel
travel_choice = date_parts.get_travel_options()

# make sure it is between 1 and 4
if date_parts.is_in_range(travel_choice, 1, 4) == False:
    travel_choice = random.randrange(1, 5)
    print('Option', travel_choice, "was picked instead.")

print(" ")

# ask user to pick second date part: dinner
dinner_choice = date_parts.get_dinner_options()

# make sure it is between 1 and 4
if date_parts.is_in_range(dinner_choice, 1, 4) == False:
    dinner_choice = random.randrange(1, 5)
    print('Option', dinner_choice, "was picked instead.")

print(" ")

# ask user to pick second date part: entertainment
entertainment_choice = date_parts.get_entertainment_options()

# make sure it is between 1 and 4
if date_parts.is_in_range(entertainment_choice, 1, 4) == False:
    entertainment_choice = random.randrange(1, 5)
    print('Option', travel_choice, "was picked instead.")

print(" ")

# print the total of all of the date parts
print("The total of your date will be: $", date_parts.get_total(travel_choice, dinner_choice, entertainment_choice), sep="")
