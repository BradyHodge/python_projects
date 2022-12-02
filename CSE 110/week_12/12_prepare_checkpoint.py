# Made by Brady Hodge
# CSE 110
# 12 Prepare: Checkpoint - finding things in the list

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

# define varables
youngest_age = float("inf")
youngest_name = ""

# Go through each person in the list
for person_line in people:

    parts = person_line.split()
    name = parts[0]
    age = int(parts[1])

    # Check if person is younger than the youngest
    if age < youngest_age:
        youngest_age = age
        youngest_name = name

# print the youngest person
print(f"The youngest person is: {youngest_name} with an age of {youngest_age}")