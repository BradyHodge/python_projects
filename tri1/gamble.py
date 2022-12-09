# use a for loop to print 10 random numbers.

import math
import random

howmany = 10
for counter in range(howmany):
    arandom = random.random()
    print(arandom)

for counter in range(howmany):
    arandom = random.randrange(25, 36)
    print(arandom)

side1 = 3
side2 = 4
hypotenuse = math.hypot(side1, side2)
print(hypotenuse)
