import re
from exceprions import *

def input_selection(range: str):
    num = input("Your selection: ")
    pattern = range + '$'
    if re.match(pattern=pattern, string=num) is None:
        raise NumberSelectionError(num)
    return num


def insert_string_int(msg: str, pattern, var):
    strint = input(msg)
    if re.match(pattern=pattern, string=strint) is None:
        raise StringError(strint, var)
    return strint


# if __name__ == '__main__':
#     input_selection("[1-6]")








