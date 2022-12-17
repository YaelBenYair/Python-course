
class BestBusCompanyExceptions(Exception):
    pass


class OutOfRangeError(BestBusCompanyExceptions):
    def __init__(self, num):
        super().__init__(f"\n{num} is out of range\n")


class FormatError(BestBusCompanyExceptions):
    def __init__(self):
        super().__init__("Incorrect format")


class StringEror(BestBusCompanyExceptions):
    def __init__(self):
        super().__init__("Input nust be string")


class BusDetaileNotExistsError(BestBusCompanyExceptions):
    def __init__(self, val):
        super().__init__(f"{val} not exists")


class BusDetaileExistsError(BestBusCompanyExceptions):
    def __init__(self, val):
        super().__init__(f"{val} already exists")


class MarkError(BestBusCompanyExceptions):
    def __init__(self, val):
        super().__init__(f"The mark {val} does not exist")

