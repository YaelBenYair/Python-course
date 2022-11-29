import random


def discount(name, last_name):
    while True:
        y_or_n = input("You have the possibility to win a discount. Want to participate in a lottery?\n"
                       "Enter 1 - for yes, 2 - for no")
        if y_or_n.isdigit() and int(y_or_n) == 1:
            return random_num(name, last_name)
        elif y_or_n.isdigit() and int(y_or_n) == 2:
            return 0
        else:
            print("\n\033[4;1;31mPlease enter a number: 1 - for yes, 2 - for no\033[1;0m")


def lucky_number_in():
    while True:
        lucky_number = input("\nEnter a number in rang 1-9\n")
        if lucky_number.isdigit() and int(lucky_number) in range(1, 10):
            return int(lucky_number)
        else:
            print("\n\033[4;1;31mPlease enter a number in range 1-9\033[1;0m")


def random_num(name, last_name):
    lucky_number = lucky_number_in()
    name_length = len(name) + len(last_name)
    rand_number = random.randrange(1, 6)
    price_count = (name_length * rand_number) % lucky_number

    if 0 < price_count <= 5:
        # price_count = price_count / 100
        return price_count / 100
    else:
        return 1


def check_rand_num(result, price):
    if result == 0:
        print("Bay Bay!")
    elif result == 1:
        print("You didn't get a discount")
    else:
        final_price = price * (1-result)
        print(f"You won a discount of {result*100}%")
        print(f"Your new price {final_price}")