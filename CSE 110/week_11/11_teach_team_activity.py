# Made by Brady Hodge
# CSE 110
# 11 Teach: Team Activity - Human Resources System

with open("hr_system.txt") as file:
    for line in file:
        line = line.strip().split()

        name = line[0]
        id_number = line[1]
        title = line[2]
        salary = float(line[3])

        pay_amount = salary / 24

        if title.lower() == "engineer":
            pay_amount += 1000

        print(f"{name} (ID: {id_number}), {title} - ${pay_amount:.2f}")