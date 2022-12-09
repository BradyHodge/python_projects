str = ('m', 'a', 'g', 'i', 'c')
str = tuple('M') + str[1:]

print(str)

peops = [('Bob', 'Smith', 1995),
         ('Tina', 'Lopez', 1993),
         ('Aru', 'Anyal', 1999)]

for person_tup in peops:
    (first_name, last_name, year_born) = person_tup
    print("{}, {}, : {}".format(last_name, first_name, year_born))
