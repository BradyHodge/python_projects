# The standard form of a quadratic equation is:
#
# ax2 + bx + c = 0, where
# a, b and c are real numbers and
# a ≠ 0
#
# Solve the quadratic equation for a = 1, b = 5, c = 6

import math

# variables
a = 1
b = 5
c = 6

# calculate when square root of b^2 - 4 * a * c is positive
pos_x = (-b + math.sqrt((b**2-(4*a*c))))/(2*a)
print("x=", pos_x)

# calculate when square root of b^2 - 4 * a * c is negative
neg_x = (-b - math.sqrt((b**2-(4*a*c))))/(2*a)
print("x=", neg_x)
