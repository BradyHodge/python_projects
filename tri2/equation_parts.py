# ----------------------
# Made by Brady Hodge
# Status: Done
# Assignment 9B; 1/2
# ----------------------

def is_numeric(char: str) -> bool:
    """checks to see if str is valid number"""
    is_true = False
    for x in range(1, 10):
        x = str(x)
        if char == x:
            is_true = True
    return is_true


def is_math_symbol(char: str) -> bool:
    """checks to see if str is valid math_symbol"""
    if char == "+":
        return True
    elif char == "-":
        return True
    elif char == "x":
        return True
    elif char == "/":
        return True
    elif char == "\\":
        return True
    elif char == "%":
        return True
    else:
        return False


def get_math_answer(start_operand: str, operator: str, end_operand: str) -> float:
    """Takes 2 numbers and an operator and does the equation"""
    math_symbol = is_math_symbol(operator)
    float_start_operand = float(start_operand)
    float_end_operand = float(end_operand)
    if math_symbol:
        if operator == "+":
            ans = float_start_operand + float_end_operand
        elif operator == "-":
            ans = float_start_operand - float_end_operand
        elif operator == "x":
            ans = float_start_operand * float_end_operand
        elif operator == "/":
            ans = float_start_operand / float_end_operand
        elif operator == "\\":
            ans = float_start_operand // float_end_operand
        elif operator == "%":
            ans = float_start_operand % float_end_operand
        else:
            ans = "There was an unexpected error with " 'get_math_answer'
            print(operator)
        return ans
    else:
        return 0

