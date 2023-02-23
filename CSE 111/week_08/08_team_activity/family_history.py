"""
Made by Brady Hodge
CSE 111
08 Team Activity: Dictionaries
"""

"""
TO DO:
    1. Within your program, the print_death_age function must print the name and age at death for each person in the people dictionary.

    2. The count_genders function must count and print the number of males and the number of females in the people dictionary.

    3. The print_marriages function must print the following for each marriage in the marriages dictionary:
        The name and age in the wedding year of the husband
        The year of the wedding
        The name and age in the wedding year of the wife

    4. Add code to the print_death_age function that prints the birth year and death year for each person.

    5. Add to your program a function named count_marriages that counts and prints the number of marriages that each person had in his or her lifetime. According to the data, who married the most times?
"""

# Each value in the people dictionary is a list. These
# are the indexes of the elements in those lists.
NAME_INDEX = 0
GENDER_INDEX = 1
BIRTH_YEAR_INDEX = 2
DEATH_YEAR_INDEX = 3

# Each value in the marriages dictionary is a list.
# These are the indexes of the elements in those lists.
HUSBAND_KEY_INDEX = 0
WIFE_KEY_INDEX = 1
WEDDING_YEAR_INDEX = 2


def main():
    people_dict = {
        # Each item in the people dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "P". Each value is a list of data about a person.
        # Each item in the dictionary is in this format:
        # person_key: [name, gender, birth_year, death_year]
        "P143": ["Lola Park", "F", 1663, 1706],
        "P338": ["Savanna Foster", "F", 1674, 1723],
        "P201": ["Tiffany Hughes", "F", 1689, 1747],
        "P203": ["Ignacio Torres", "M", 1693, 1758],
        "P128": ["Yasmin Li", "F", 1701, 1716],
        "P342": ["Trent Ross", "M", 1705, 1757],
        "P202": ["Samyukta Nguyen", "M", 1717, 1774],
        "P132": ["Joel Johnson", "M", 1724, 1800],
        "P445": ["Whitney Nelson", "F", 1757, 1823],
        "P318": ["Khalid Ali", "M", 1759, 1814],
        "P317": ["Davina Patel", "F", 1775, 1860],
        "P313": ["Enzo Ruiz", "M", 1782, 1782],
        "P475": ["Lauren Smith", "F", 1800, 1802],
        "P455": ["Lucas Ross", "M", 1800, 1853],
        "P435": ["Jamal Gray", "M", 1810, 1831],
        "P204": ["Fatima Soares", "F", 1812, 1898],
        "P206": ["Ephraim Foster", "M", 1831, 1885],
        "P500": ["Peter Price", "M", 1832, 1878],
        "P207": ["Rosalina Jimenez", "F", 1875, 1956],
        "P425": ["Rachel Johnson", "F", 1876, 1940],
        "P121": ["Vanessa Bennet", "F", 1880, 1960],
        "P152": ["Jose Castillo", "M", 1884, 1931],
        "P205": ["Liam Myers", "M", 1902, 1950],
        "P465": ["Isabella Lopez", "F", 1907, 1959],
        "P168": ["Megan Anderson", "F", 1909, 1945]
    }

    marriages_dict = {
        # Each item in the marriages dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "M". Each value is a list of data about a marriage.
        # Each item in the dictionary is in this format:
        # marriage_key: [husband_key, wife_key, wedding_year]
        "M48": ["P203", "P201", 1711],
        "M45": ["P342", "P338", 1722],
        "M36": ["P203", "P201", 1724],
        "M47": ["P202", "P445", 1774],
        "M21": ["P132", "P445", 1775],
        "M59": ["P132", "P317", 1792],
        "M63": ["P318", "P445", 1804],
        "M12": ["P318", "P317", 1808],
        "M54": ["P435", "P204", 1830],
        "M34": ["P455", "P204", 1853],
        "M55": ["P500", "P317", 1859],
        "M52": ["P206", "P204", 1875],
        "M78": ["P152", "P121", 1905],
        "M50": ["P152", "P425", 1917],
        "M64": ["P205", "P465", 1925],
        "M62": ["P152", "P207", 1925],
        "M70": ["P152", "P168", 1928]
    }

    # Call the print_death_age function to print
    # each person's name and age at death.
    print_death_age(people_dict)

    # Print a blank line.
    print()

    # Call the count_genders function to count
    # and print the number of males and females.
    count_genders(people_dict)

    # Print a blank line.
    print()

    # Call the print_marriages function to print
    # human readable data about the marriages.
    print_marriages(marriages_dict, people_dict)

    print()
    count_marriages(marriages_dict, people_dict)

def print_death_age(people_dict):
    """For each person in the people dictionary,
    print the person's name and age at death.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    print("Age at Death, birth year, death year")
    for person_key in people_dict:
        person = people_dict[person_key]
        name = person[0]
        birth_year = person[2]
        death_year = person[3]
        age_at_death = death_year - birth_year
        print(name, age_at_death, birth_year, death_year)


def count_genders(people_dict):
    """Count and print the number of males
    and females in the people dictionary.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    male = 0
    female = 0

    for person_key in people_dict:
        person = people_dict[person_key]
        gender = person[1]
        
        if gender.upper() == "F":
            female += 1
        elif gender.upper() == "M":
            male += 1
        else:
            print("There was an error with the count_genders function.")
    print("Genders")
    print("Number of males:", male)
    print("Number of females", female)
    


def print_marriages(marriages_dict, people_dict):
    """For each marriage in the marriages dictionary, print
    the husband's name, his age at wedding, the wedding year,
    the wife's name, and her age at wedding.

    Parameters
        marriages_dict: a dictionary that contains data about
            marriages. Each item in the dictionary is in this format:
            marriage_key: [husband_key, wife_key, wedding_year]
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    print("Marriages")
    for marriage_key in marriages_dict:
        marriage = marriages_dict[marriage_key]
        husband_key = marriage[0]
        wife_key = marriage[1]
        wedding_year = marriage[2]

        husband = people_dict[husband_key]
        husband_name = husband[0]
        husband_birth_year = husband[2]
        husband_age_at_wedding = wedding_year - husband_birth_year

        wife = people_dict[wife_key]
        wife_name = wife[0]
        wife_birth_year = wife[2]
        wife_age_at_wedding = wedding_year - wife_birth_year

        print(husband_name, husband_age_at_wedding, ">", wedding_year, "<", wife_name, wife_age_at_wedding,)

def count_marriages(marriages_dict, people_dict):
    """Counts and prints the number of marriages that each person 
    had in his or her lifetime. According to the data, who married 
    the most times?

    Parameters
        marriages_dict: a dictionary that contains data about
            marriages. Each item in the dictionary is in this format:
            marriage_key: [husband_key, wife_key, wedding_year]
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    counts = {}
    print("Marriage Counts")
    for marriage in marriages_dict.values():
        person1, person2, _ = marriage
        counts[person1] = counts.get(person1, 0) + 1
        counts[person2] = counts.get(person2, 0) + 1

    print(max(counts, key=counts.get))
    

    


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
