# Made by Brady Hodge
# CSE 110
# 06 Teach: Team Activity - Amusement Park Rides

first_can_ride = False
second_can_ride = False

first_rider_age = int(input("What is the age of the first rider? "))
first_rider_height = int(input("What is the height of the first rider? "))

is_second_rider = input("Is there a second rider (yes/no)? ").lower()
if is_second_rider.strip() == "yes":
    second_rider = True
    second_rider_age = int(input("What is the age of the second rider? "))
    second_rider_height = int(input("What is the height of the second rider?"))
elif is_second_rider.strip() == "no":
    second_rider = False
else:
    print("Sorry, I didn't understand that, try again.")

if first_rider_age > 17 and first_rider_height

# check if first rider is above 36 in
if first_rider_height > 36:
    first_can_ride = True
elif first_rider_height < 36:
    first_can_ride = False
else:
    print("Something has gone wrong, why would you do this?")

# check if second rider is above 36 in (if second rider is True)
if second_rider:
    if second_rider_height > 36:
        second_can_ride = True
    elif second_rider_height < 36:
        second_can_ride = False
    else:
        print("Something has gone wrong, why would you do this?")

# Print result 
if second_rider:
    if first_can_ride and second_can_ride:
        print("Welcome to the ride. Please be safe and have fun!")
    elif first_can_ride and not second_can_ride:
        print("Only the first person may ride, sorry.")
    elif not first_can_ride and second_can_ride:
        print("Only the second person may ride, sorry.")
    elif not first_can_ride and not second_can_ride:
        print("Nether one of you can ride, sorry.")
    else:
        print("Something has gone horribly wrong, how have you managed to do this?")
else:
    if first_can_ride:
        print("Welcome to the ride. Please be safe and have fun!")
    elif not first_can_ride:
        print("Sorry, you may not ride.")
    else:
        print("Something has gone horribly wrong, how have you managed to do this?")
