# --------------------
# Made by Brady Hodge
# Status: In Progress
# Assignment 6D pt 1 of 2
# --------------------

import random


def classify_timecard(hours_worked):
    """accepts the number of hours worked and classifies if the employee is part, full, or over-time"""
    if 20 > hours_worked:
        return "part-time"
    elif 20 > hours_worked <= 40:
        return "full-time"
    elif 40 < hours_worked:
        return "over-time"
    else:
        print("function 'classify_timecard' failed")


def get_pay_rate():
    """20% chance of returning 38.56,
    20% chance or returning 20.20,
    60% chance of returning 12.35
    as an hourly rate for an employee"""
    percent = random.randrange(0, 10)
    if percent < 2:
        return 38.56
    elif 2 <= percent < 4:
        return 20.12
    elif 4 <= percent < 10:
        return 12.35
    else:
        print("function 'get_pay_rate' failed")


def get_hours_worked():
    """25% chance of picking a number between 10 and 35(exclusive),
    50% chance of picking a number between 20 and 40(exclusive),
    25% chance of picking a number between 30 and 60(exclusive),
    as the number of hours worked for an employee"""

    percent = random.randrange(0, 100)
    if percent < 25:
        return random.randrange(10.0, 35.0)
    elif 25 <= percent < 75:
        return random.randrange(20.0, 40.0)
    elif 75 <= percent < 100:
        return format(random.randrange(30.0, 60.0), ".1f")
    else:
        print("function 'get_hours_worked' failed")


def is_in_range(val_test, val_min, val_max):
    """tests number val_test to see if it is within the range of val_min and val_max
    and returns as a boolean"""
    val_range = val_min <= val_test <= val_max
    return val_range
