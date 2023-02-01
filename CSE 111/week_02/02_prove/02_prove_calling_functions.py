"""
Made by Brady Hodge
CSE 111
02 Prove: Calling Functions
"""

# Get pi to use in the colume calculations
from math import pi

# get datetime to add date and time to log file
from datetime import datetime

# Get the user's input for the volume calculations
tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
wheel_diameter = int(
    input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the volume of the tire
approximate_volume = (pi * tire_width ** 2 * aspect_ratio *
                      (tire_width * aspect_ratio + 2540 * wheel_diameter)) / 10000000000

# Print the answer
print(f"\nThe approximate volume is {approximate_volume:.2f} liters\n")

# Ask the user if they want to buy tires

if tire_width == 205 and aspect_ratio == 60 and wheel_diameter == 15:
    tire_price = 100

elif tire_width == 215 and aspect_ratio == 65 and wheel_diameter == 16:
    tire_price = 120
elif tire_width == 225 and aspect_ratio == 70 and wheel_diameter == 17:
    tire_price = 140
else:
    tire_price = "Not available"
print(f"The price for these tires is: {tire_price}")

buy_tires = input("Would you like to buy these tires? (yes/no): ")

if buy_tires == "yes":
    phone_number = input("Please enter your phone number: ")
    with open("volumes.txt", "at") as log_file:
        log_file.write(f"{phone_number}\n")


# Get the current date and time
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

# append to a log file named volumes.txt
with open("volumes.txt", "at") as log_file:
    log_file.write(f"{current_date_and_time}, {tire_width}, {aspect_ratio}, {wheel_diameter}, {approximate_volume:.2f}\n")
