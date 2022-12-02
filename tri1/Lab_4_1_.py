# --------------------
# Made by Brady Hodge
# Status: Graded
# --------------------

def letterGrade(n):
    """Returns a letter grade based on test score n"""
    if n >= 90:
        grade = "A"
    elif n >= 80:
        grade = "B"
    elif n >= 70:
        grade = "C"
    elif n >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade


mark = float(input("What score did you get on your test? "))

print("You received a letter grade of", letterGrade(mark))
