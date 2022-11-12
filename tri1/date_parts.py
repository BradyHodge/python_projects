# --------------------
# Made by Brady Hodge
# Status: Done
# Lab 6C pt 1 of 2
# --------------------

def get_travel_options():
    """prompts the user with the travel options for the date"""
    print("Your options for travel are:")
    print('     1: Bus – cost: $2.00 (nothing says romance like riding public transit.)')
    print('     2: Bicycle – cost: $21.20 (to rent a bicycle for two)')
    print('     3: Car – cost: $5.00 (to cover your gas)')
    print('     4: Carriage Ride – cost: $84.80 (for the service)')
    print(" ")
    option = int(input("How will you travel on your date? "))
    print(" ")
    if option == 1:
        print("You chose option 1: Bus")
    elif option == 2:
        print("You chose option 2: Bicycle")
    elif option == 3:
        print("You chose option 3: Car")
    elif option == 4:
        print("You chose option 4: Carriage")
    else:
        print("Invalid choice:")

    return option


def get_dinner_options():
    """prompts the user with the dinner options for the date"""
    print("Your options for dinner are:")
    print('     1: Nowhere – cost: $0 (this is just a date, who said anything about dinner. You are a poor college '
          'student after all. I am sure your date will understand.)')
    print('     2: McDonalds – cost: $14.82 (not very romantic nor requires a tip. At least you went out to dinner.)')
    print('     3: Applebee’s – cost: $27.98 (better than McDonalds. The tip, and tax are included in this price.)')
    print('     4: SandPiper’s – cost: $70.21 (going all out for Pocatello, you must really like this person. The tip, '
          'and tax are included in this price.)')
    print(" ")
    option = int(input("Where will you go to dinner? "))
    print(" ")
    if option == 1:
        print("You chose option 1: Nowhere")
    elif option == 2:
        print("You chose option 2: McDonalds")
    elif option == 3:
        print("You chose option 3: Applebee's")
    elif option == 4:
        print("You chose option 4: SandPiper's")
    else:
        print("Invalid choice:")
    return option


def get_entertainment_options():
    """prompts the user with the entertainment options for the date"""
    print("Your entertainment options are:")
    print('     1: Take a walk – cost: None (Romantic and Free!)')
    print('     2: Bowling – cost: $8.50 (includes shoes; no refunds for gutter balls)')
    print('     3: Movie – cost:  $26.06 (the classic overpriced entertainment)')
    print('     4: Miniature Golf – cost: $10.60 (18 holes of fun)')
    print(" ")
    option = int(input("What will you do after dinner? "))
    print(" ")
    if option == 1:
        print("You chose option 1: Take a walk")
    elif option == 2:
        print("You chose option 2: Bowling")
    elif option == 3:
        print("You chose option 3: Movie")
    elif option == 4:
        print("You chose option 4: Miniature Golf")
    else:
        print("Invalid choice:")
    return option


def is_in_range(val_test, val_min, val_max):
    """tests number val_test to see if it is within the range of val_min and val_max and returns boolean"""
    val_range = val_min <= val_test <= val_max
    return val_range


def get_price(date_part, option):
    """accepts the date part and number and returns a price in a float"""
    date_part = str(date_part)
    option = int(option)
    price = float(0.00)

    if date_part == 'a':
        if option == 1:
            price = 2.00
        elif option == 2:
            price = 21.20
        elif option == 3:
            price = 5.00
        elif option == 4:
            price = 84.80
        else:
            print("function get_price_a failed")
    elif date_part == 'b':
        if option == 1:
            price = 0.00
        elif option == 2:
            price = 14.82
        elif option == 3:
            price = 27.82
        elif option == 4:
            price = 70.21
        else:
            print("function get_price_b failed")
    elif date_part == 'c':
        if option == 1:
            price = 0.00
        elif option == 2:
            price = 8.50
        elif option == 3:
            price = 26.06
        elif option == 4:
            price = 10.60
        else:
            print("function get_price_c failed")
    else:
        print("function get_price failed")
    return price


def get_total(option_travel, option_dinner, option_entertainment):
    """adds up all of the costs from the get_price function"""
    total_price = float(0.00)
    total_price = total_price + get_price('a', option_travel)
    total_price = total_price + get_price('b', option_dinner)
    total_price = total_price + get_price('c', option_entertainment)
    return format(total_price, ".2f")
