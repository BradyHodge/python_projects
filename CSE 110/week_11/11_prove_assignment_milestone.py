# Made by Brady Hodge
# CSE 110
# 11 Prove: Assignment Milestone - Life Expectancy Data

# difine varables
largest_life = float('-inf')
smallest_life = float('inf')
line_numb = 0

# open file and save as f
with open("life-expectancy.csv") as f:
    for line in f:

        # keep count of the line number
        line_numb += 1

        # skip the first line
        if line_numb != 1:
            line = line.strip().split(",")

            # get the year, life expectancy and conuntry
            country = line[0]
            year = line[2]
            life_expectancy = float(line[3])

            # find the max life expectancy
            if largest_life <= life_expectancy:
                largest_life = life_expectancy
                largest_country = country
                largest_year = year

            # find the min life expectancy
            if smallest_life >= life_expectancy:
                smallest_life = life_expectancy
                smallest_country = country
                smallest_year = year

    # print the overal life expectency
    print(f"The overall max life expectancy is: {largest_life} form {largest_country} in {largest_year}")
    print(f"The overall min life expectancy is: {smallest_life} form {smallest_country} in {smallest_year}")