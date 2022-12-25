import re

import requests

#
def cpital_and_lower(word: str):
    if re.match("[A-Z][a-z]", word) is None:
        raise Exception()


li = ["Dog", "BBg", "fHp", "sDfg", "DfFg"]
for word in li:
    try:
        cpital_and_lower(word)
        print(word)
    except Exception:
        print(f" The word '{word}' is not a capitalized word")







