# write a function find hypot. The function will be given the length if two
# of a right-angled triable and it should return the length of the hypotenuse
# Hint x**0.5 will return the sqare root or use sqrt

def findHypot(side1, side2):
    side3_sq = side1 ** 2 + side2 ** 2
    side3 = side3_sq ** 0.5
    return side3


def is_rightangled(side1, side2, side3):
    if side3**2 == side1**2 + side2**2:
        print("Ture")
    else:
        print("False")

side1 = 6
side2 = 10
side3 = 5


is_rightangled(side1, side2, side3)