
class CocktailsAndGamesExeption(Exception):
    pass


class DateNotFoundError(CocktailsAndGamesExeption):
    pass


class StatusCodeError(CocktailsAndGamesExeption):
    def __init__(self, status):
        super().__init__(f"There is an error: {status}")


class NumberSelectionError(CocktailsAndGamesExeption):
    def __init__(self, num):
        super().__init__(f"The number {num} not in range")


class StringError(CocktailsAndGamesExeption):
    def __init__(self, strs, string_int: str):
        super().__init__(f"{strs} must be {string_int}")