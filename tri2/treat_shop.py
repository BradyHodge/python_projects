# ----------------------
# Made by Brady Hodge
# Status: In Progress
# Assignment 13B; 2/2
# Script
# ----------------------

import treats

treats_list = treats.get_inventory()
keep_going = True

def get_brownie():
    treat_name = "Brownie"
    brownie_cals = input('How many calories are in the Brownie? ')
    has_nuts = input('Does the Brownie have nuts(y/n)? ')
    has_nuts = has_nuts.lower()
        if has_nuts == 'y':
            has_nuts = True
        elif has_nuts == 'n':
            has_nuts = False
        elif:
            print('Please input a valid value.')
    return treats.Brownie(brownie_cals, has_nuts)


while keep_going:
    user_option = input(
        'What would you like to do?\n    a - Add a treat to the inventory\n    l - List all treats in the inventory.\n   x - exit the application.\n')
    user_option = user_option.lower()
    if user_option == 'a':
        valid_input = False
        while valid_input != True:
            item_to_add = input(
                'What treat would you like to add?\n    b - Brownie\n    c - Cookie\n    t - Taffy, o - Other Treat\n    n - Never mind\n')
            item_to_add = item_to_add.lower()
            if item_to_add == 'b':
                treats_list.append(get_brownie())
                valid_input = True
            elif item_to_add == 'c':
                print('c')
                valid_input = True
            elif item_to_add == 't':
                print('c')
                valid_input = True
            elif item_to_add == 'o':
                print('c')
                valid_input = True
            elif item_to_add == 'n':
                break
            else:
                print('There was a problem, try a valid input.')
    elif user_option == 'l':
        inventory = treats.Treat.get_inventory()
        print(inventory)
    elif user_option == 'x':
        print('Goodbye')
        keep_going = False
        break
    else:
        print('There was an error')