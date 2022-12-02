# --------------------
# Made by Brady Hodge
# Status: Done
# --------------------


# Ask the user for their name
user_name = input("What is your name? ")

# Ask the user for their height in inches
height = float(input("What is your height in inches? "))

# Ask the user for their weight in pounds
weight = float(input("What is your weight in pounds? "))


# convert to feet and inches
height_ft = height // 12
height_in = height % 12

# convert to metric
weight_kg = weight / 2.2046
height_m = height / 39.37

# Calculate BMI
bmi = 1.3 * (weight_kg / (height_m ** 2.5))


# round
bmi = round(bmi, 2)
weight_kg = round(weight_kg, 2)
height_m = round(height_m, 2)
weight = round(weight, 0)
weight = int(weight)
height_ft = int(height_ft)
height_in = int(height_in)

# display BMI
print(user_name, "you are", height_ft, "feet", height_in, "inches tall and weigh", weight, "pounds.")
print("That converts to", height_m, "meters and", weight_kg, "kilograms.")
print("Your BMI is", bmi)
