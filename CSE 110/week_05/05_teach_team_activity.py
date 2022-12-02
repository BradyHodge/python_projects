# Made by Brady Hodge
# CSE 110
# 05 Teach: Team Activity - Grade Calculator

# CORE REQUIREMENTS
# Ask the user for their grade percentage, then write a series of if-elif-else statements to print out the appropriate letter grade. (At this point, you'll have a separate print statement for each grade letter in the appropriate block.)
grade_percentage = float(input("Enter your grade percentage: "))

if grade_percentage >= 90:
    grade_letter = "A"

elif grade_percentage >= 80:
    grade_letter = "B"

elif grade_percentage >= 70:
    grade_letter = "C"

elif grade_percentage >= 60:
    grade_letter = "D"

elif grade_percentage < 60:
    grade_letter = "F"

else:
    print("Something has gone wrong. Maybe try again.")


if grade_percentage < 97 and grade_percentage >= 60:
    if (grade_percentage % 10) >= 7:
        grade_sign = "+"

    elif (grade_percentage % 10) < 3:
        grade_sign = "-"
    else:
        grade_sign = ""
else:
        grade_sign = ""


print(f"Your grade is {grade_letter}{grade_sign}")

# Assume that you must have at least a 70 to pass the class. After determining the letter grade and printing it out. Add a separate if statement to determine if the user passed the course, and if so display a message to congratulate them. If not, display a different message to encourage them for next time.
if grade_percentage >= 70:
    print("Congratulations! You passed the course.")
elif grade_percentage < 70:
    print("Unfortunately, you did not pass the course. Don't worry, im sure you will ace the class next time!")
else:
    print("Something has gone wrong. Maybe try again.")

# Change your code from the first part, so that instead of printing the letter grade in the body of each if, elif, or else block, instead create a new variable called letter and then in each block, set this variable to the appropriate value. Finally, after the whole series of if-elif-else statements, have a single print statement that prints the letter grade once.

# STRETCH CHALLENGE
# Add to your code the ability to include a "+" or "-" next to the letter grade, such as B+ or A-. For each grade, you'll know it is a "+" if the last digit is >= 7. You'll know it is a minus if the last digit is < 3 and otherwise it has no sign.

# After your logic to determine the grade letter, add another section to determine the sign. Save this sign into a variable. Then, display both the grade letter and the sign in one print statement.

# Hint: To get the last digit, you could divide the number by 10, and get the remainder. You might refer back to the preparation material for Lesson 03 to see the operators and find the one that does division and gives you the remainder.

# At this point, don't worry about the exceptional cases of A+, F+, or F-.

# Recognize that there is no A+ grade, only A and A-. Add some additional logic to your program to detect this case and handle it correctly.

# Similarly, recognize that there is no F+ or F- grades, only F. Add additional logic to your program to detect these cases and handle them correctly.
