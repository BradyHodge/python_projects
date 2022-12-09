def isPalindrome(string):
    if len(string) > 1:
        if string[0] == string[-1]:
            return isPalindrome(string[1:-1])
        else:
            return False
    return True


def isPalindrome(string):
    reversedString = string[::-1]
    return string == reversedString