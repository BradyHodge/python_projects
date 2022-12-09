# Made by Brady Hodge
# CSE 110
# 02 Teach: Programming Activity

print("Please enter the following information:\n")

first_name = input("First name: ")
last_name = input("Last name: ")
email_address = input("Email address: ")
phone_number = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID Number: ")

hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
month_started = input("Starting Month: ")
training = input("Completed additional training? ")

print("\nThe ID Card is:")
print("-" * 40)
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(job_title.title())
print(f"ID: {id_number}")
print()
print(email_address.lower())
print(phone_number)
print("")

print(f"Hair: {hair_color:15} Eyes: {eye_color}")
print(f"Month: {month_started:14} Training: {training}")
print("-" * 40)
