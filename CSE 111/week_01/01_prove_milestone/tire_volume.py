"""
Made by Brady Hodge
CSE 111
01 Prove Milestone: Review Python
"""

# Get pi to use in the colume calculations
from math import pi

# Get the user's input for the volume calculations
tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
wheel_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the volume of the tire
approximate_volume = (pi * tire_width ** 2 * aspect_ratio * (tire_width * aspect_ratio + 2540 * wheel_diameter))/ 10000000000

# Print the answer
print(f"\nThe approximate volume is {approximate_volume:.2f} liters\n")