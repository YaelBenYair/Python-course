
# ------------------ 1 -------------------
def past(words: list[str]) -> list:
    past_tense = []
    for word in words:
        if word[-1:-3:-1] != 'de':
            if word[-1] == 'e':
                word += 'd'
            else:
                word += 'ed'
        past_tense.append(word)
    return past_tense

# ------------------ 2 -------------------
def rain(rain_f: str, min_rain: int) -> int:
    num_rainy_months: int = 0

    rain_f = "".join(rain_f.split())
    rain_f = rain_f.split(",")

    for dg in rain_f:
        if float(dg) > min_rain:
            num_rainy_months += 1

    return num_rainy_months







if __name__ == '__main__':
    pass

    a = ['adopt', 'bake', 'beam', 'cook', 'time', 'grill', 'waved', 'hire']
    print(past(a))

    mi = '45, 65, 70.4, 82.6, 20.1, 90.8, 76.1, 30.92, 46.8, 67.1, 79.9'
    print(rain(mi, 75))



