# --------------------
# Made by Brady Hodge
# Status: Graded
# --------------------

import random


def get_single_pin(x):
    if x == 1:
        a = 1
        b = 9
    elif x == 2:
        a = 10
        b = 99
    elif x == 3:
        a = 100
        b = 999
    elif x == 4:
        a = 1000
        b = 9999
    elif x == 5:
        a = 10000
        b = 99999
    elif x == 6:
        a = 100000
        b = 999999
    else:
        a = 0
        b = 0

    pin = random.randrange(a, b)
    return pin


def get_number_of_pins():
    pin_num = int(input("How many pins do you need generated? "))
    pin_digits = int(input("How many digits in each pin? "))
    for number in range(pin_num):
        print(get_single_pin(pin_digits))


get_number_of_pins()
