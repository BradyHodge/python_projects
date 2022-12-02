# Made by Brady Hodge
# CSE 110
# 12 Prove: Assignment - Life Expectancy Data

"""
Identify the year and country that has the largest drop from one year to the next.

Allow the user to type in a country, then show the minimum, maximum, and average life expectancy for that country.

Look for interesting anomalies or patterns in the data.

Find another dataset and work with it.

Anything else you can think of!
"""

# difine varables
largest_life = float("-inf")
smallest_life = float("inf")
line_numb = 0

# get the year of interest from the user
year_of_interest = int(input("Enter the year of interest: "))

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
print(f"\nThe overall max life expectancy is: {largest_life} form {largest_country} in {largest_year}")
print(f"The overall min life expectancy is: {smallest_life} form {smallest_country} in {smallest_year}")

# reset varables
largest_life = float('-inf')
smallest_life = float('inf')
line_numb = 0
numb_of_countries = 0
life_expectancies = []
average_life = 0

print(f"\nFor the year {year_of_interest}:")

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
            year = int(line[2])
            life_expectancy = float(line[3])

            if year_of_interest == year:
                
                # count the numb of countries for the average
                numb_of_countries += 1

                # add the life expectancy to the list
                life_expectancies.append(life_expectancy)

                # find the max life expectancy
                if largest_life <= life_expectancy:
                    largest_life = life_expectancy
                    largest_country = country

                # find the min life expectancy
                if smallest_life >= life_expectancy:
                    smallest_life = life_expectancy
                    smallest_country = country

    # find the average life expectancy
    for numb in life_expectancies:
        average_life += numb
    average_life = average_life / numb_of_countries

    # print the year of interest
    print(f"The average life expectancy across all countries was {average_life:.2f}")
    print(f"The max life expectancy was in {largest_country} with {largest_life}")
    print(f"The min life expectancy was in {smallest_country} with {smallest_life}")