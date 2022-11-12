# --------------------
# Made by Brady Hodge
# Status: Done
# --------------------

import random


def get_year_born():
    """prompts the user for the year they were born"""
    year_born = int(input("What year where you born? "))
    return year_born


def get_number_to_show():
    """ prompts the user for the number of date and time pairs to show"""
    numb_to_show = int(input("How many date/times should I show? "))
    return numb_to_show


def get_random_time():
    """ returns a string representation of a random time in 24-hour format"""
    rand_hour = str(random.randrange(0, 24))
    rand_min = str(random.randrange(0, 60))
    rand_hour = rand_hour.zfill(2)
    rand_min = rand_min.zfill(2)
    rand_time = rand_hour + ":" + rand_min
    return rand_time


def get_random_date(x):
    """ accepts the year the user was born and returns a string representation of a random date
    between the birth year and the current year"""
    rand_month = str(random.randrange(1, 13)).zfill(2)
    rand_day = str(random.randrange(1, 29)).zfill(2)
    rand_year = str(random.randrange(x, 2021))
    rand_date = rand_month + "/" + rand_day + "/" + rand_year
    return rand_date


user_year_born = get_year_born()
numb_of_dates = get_number_to_show()

print(" ")
print("Here are some possible times in your life:")
print("         Date            Time")
for y in range(numb_of_dates):
    date = get_random_date(user_year_born)
    time = get_random_time()
    print("     ", date, "      ", time)
