from BestBusCompanyExceptions import OutOfRangeError, StringEror


def selection(msg: str, maxi: int) -> int:
    while True:
        selection = int(input(msg))
        if selection < 1 or selection > maxi:
            raise OutOfRangeError(selection)
        return selection


def insert_origin_destin(msg) -> str:
    while True:
        stop_in = input(msg).strip().capitalize()
        stop = "".join(stop_in.split(" "))
        stop = "".join(stop.split("-"))
        if stop.isalpha():
            return stop_in
        raise StringEror()








