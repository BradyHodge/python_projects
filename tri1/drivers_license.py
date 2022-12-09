age = float(input("What is your age? "))

print("You are able to receive")
if age >= 18:
    print("Unrestricted Driver's License")
elif age >= 15:
    print("Underage Driver's License")
elif age >= 14.5:
    print("Supervised Instruction Permit")
else: print("No License")
