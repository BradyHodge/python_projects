# return the sum of all integer numbers up to and including n.

import math

def sumTo(n):
    num = (n*(n+1))/2
    return num

def areaOfCircle(r):
    area = math.pow(r, 2) * math.pi
    return area

print(areaOfCircle(10))