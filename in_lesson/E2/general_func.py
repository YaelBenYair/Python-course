import re
from exeprions import *

def input_selection(range: str):
    num = input("Your selection: ")
    pattern = range + '$'
    if re.match(pattern=pattern, string=num) is None:
        raise NumberSelectionError(num)
    return num


def insert_string_int(msg: str, pattern):
    strint = input(msg)
    if re.match(pattern=pattern, string=strint) is None:
        raise StringError(strint)
    return strint


# if __name__ == '__main__':
#     input_selection("[1-6]")








