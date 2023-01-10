# Made by Brady Hodge
# CSE 111
# 01 Checkpoint: Review Python

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

# Get age from user as int
age = int(input("Please enter your age: "))

# Compute max and min beneficial heart rates of user's age.
max_rate = 220 - age
slowest = max_rate * 0.65
fastest = max_rate * 0.85

# Print a message for the user to see.
print(f"When you exercise to strengthen your heart, you should keep your heart rate between {slowest:.0f} and {fastest:.0f} beats per minute.")