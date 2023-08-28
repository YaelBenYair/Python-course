
# ------------------ 1A -------------------
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

# ------------------ 1B -------------------
def rain(rain_f: str, min_rain: int) -> int:
    num_rainy_months: int = 0

    rain_f = "".join(rain_f.split())
    rain_f = rain_f.split(",")

    for dg in rain_f:
        if float(dg) > min_rain:
            num_rainy_months += 1

    return num_rainy_months


# ------------------ 2A -------------------
class AppleBasket:

    def __init__(self, color: str, num: int):
        self.num = num
        self.color = color

    def __str__(self):
        return f"A basket of {self.num} {self.color} apples."

    def increase(self):
        self.num += 1


# ------------------ 2B -------------------
class BankAccount:

    def __init__(self, name: str, amt: float):
        self.name = name
        self.amt = amt

    def __str__(self):
        return f"Your account, {self.name}, has {self.amt} dollars."





if __name__ == '__main__':
    pass
    # --1A--
    # a = ['adopt', 'bake', 'beam', 'cook', 'time', 'grill', 'waved', 'hire']
    # print(past(a))
    #
    # --1B--
    # mi = '45, 65, 70.4, 82.6, 20.1, 90.8, 76.1, 30.92, 46.8, 67.1, 79.9'
    # print(rain(mi, 75))

    # --2A--
    app = AppleBasket('red', 2)
    app.increase()
    app.increase()
    print(app)

    app_2 = AppleBasket('blue', 50)
    print(app_2)

    t1 = BankAccount('Bob', 100)
    print(t1)



