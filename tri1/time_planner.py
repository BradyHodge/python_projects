# --------------------
# Made by Brady Hodge
# Status: In Progress
# Assignment 6D pt 2 of 2
# --------------------

import planner_data
import random

numb_of_employees = int(input("How many employees do you have? "))

if planner_data.is_in_range(numb_of_employees, 1, 20) == False:
    numb_of_employees = random.randrange(1, 21)
    print("out side of range:", numb_of_employees, "was picked instead.")


hours_worked = str(planner_data.get_hours_worked())
for a in range(numb_of_employees - 1):
    hours_worked = hours_worked + ", " + str(planner_data.get_hours_worked())


pay_rate = str(planner_data.get_pay_rate())
for b in range(numb_of_employees - 1):
    pay_rate = pay_rate + ", " + str(planner_data.get_pay_rate())


employee_number = 0
for c in list(hours_worked):
    employee_number = employee_number + 1
    print("employee number", employee_number)
    print(c)
