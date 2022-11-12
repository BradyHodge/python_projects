# ----------------------
# Made by Brady Hodge
# Status: Done
# lab 10-6; 1/1
# ----------------------

def get_count(input_list, char):
    counter = 0
    for i in input_list:
        if i == char:
            counter += 1
    if counter == 0:
        for j in range(len(input_list)):
            x = input_list[j].count(char)
            counter += x
    return counter


def is_in(input_list, input_object):
    for i in input_list:
        if i == input_object:
            return True
    return False


def get_reverse(input_list):
    first = 0
    last = len(input_list) - 1
    while first < last:
        input_list[first], input_list[last] = input_list[last], input_list[first]
        first += 1
        last -= 1
    return input_list


def do_index(input_list, input_object):
    for x in range(len(input_list)):
        if input_list[x] == input_object:
            return x
    return -1


def do_insert(input_list, index, input_object):
    return input_list[:index] + [input_object] + input_list[index:]


print("get_count:")
print(get_count(["hello", "jeff", "get", "fun", "pickle", "secret", "snugly", "lies"], "pickle"))
print("is_in:")
print(is_in(["hello", "jeff", "get", "fun", "pickle", "secret", "snugly", "lies"], "lies"))
print("get_reverse:")
print(get_reverse(["hello", "jeff", "get", "fun", "pickle", "secret", "snugly", "lies"]))
print("do_index:")
print(do_index(["hello", "jeff", "get", "fun", "pickle", "secret", "snugly", "lies"], "lies"))
print("do_insert:")
print(do_insert(["hello", "jeff", "get", "fun", "pickle", "secret", "snugly", "lies"], 3, "people"))
