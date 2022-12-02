# ----------------------
# Made by Brady Hodge
# Status: In Progress
# Assignment ?; 1/1
# ----------------------

def remove_dups(str_in: str) -> str:
    ch_list = []
    str_out = ''
    for ch in str_in:
        if ch in ch_list:
            continue
        elif ch not in ch_list:
            str_out += ch
            ch_list.append(ch)
    return str_out


user_str = str(input("Remove duplicate letters in: "))
print(remove_dups(user_str))
