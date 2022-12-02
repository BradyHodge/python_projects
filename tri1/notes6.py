lines = 0


def get_left_pyramid(lines):
    for row in range(lines):
        str = " "
        for col in range(lines):
            if col <= row:
                str += "*"
            else:
                str += " "
        print(str)

def get_right_pyramid(lines):
    for row in range(lines):
        str = " "
        for col in range(lines):
            if col >= row:
                str += " "
            else:
                str += "*"
        print(str)

get_right_pyramid(lines)
get_right_pyramid(lines)