# --------------------
# Made by Brady Hodge
# Status: Graded
# --------------------

import random


def get_number_to_generate():
    """prompts the user for the number of phone numbers to generate"""
    numb_of_numb = int(input("How many phone numbers should I show? "))
    return numb_of_numb


def get_line_number():
    """returns an integer representation of a line number in the range"""
    line_numb = int(random.randrange(0, 10000))
    return line_numb


def get_area_code(n):
    """accepts an integer of the starting number of the area code
    and returns an integer representation of an area code"""
    min_val = n * 100
    max_val = n * 100 + 20
    area_code = int(random.randrange(min_val, max_val))
    return area_code


def get_office_code(x):
    """ accepts an integer of the starting number of the office code
    and returns an integer representation of an office code"""
    min_val = x * 100 + 20
    max_val = x * 100 + 100
    office_code = int(random.randrange(min_val, max_val))
    return office_code


# ask user for numb of numb
numb_to_gen = get_number_to_generate()

# print message
print(" ")
print("Here are the", numb_to_gen, "random phone numbers.")

# generate and print rand numbs
for y in range(numb_to_gen):
    # gets area code
    rand_numb_area = random.randrange(2, 10)
    area = get_area_code(rand_numb_area)

    # makes sure the area code is not 911
    if area == 911:
        area = area + 1
    else:
        area = area

    # gets office code
    rand_numb_office = random.randrange(2, 10)
    office = get_office_code(rand_numb_office)

    # gets line number and converts to a string so str.zfill can be used later
    line = str(get_line_number())

    # prints phone numbers
    print("     ", "(", area, ")", " ", office, "-", line.zfill(4), sep="")
