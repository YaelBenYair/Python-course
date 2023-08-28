from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name: str|None = None, profession: str|None = None):
        self.name = name
        self.profession = profession

    def __str__(self):
        return f"name: {self.name} profession: {self.profession}"

    def display(self):
        return f"{self.__class__.__name__} class"

    @abstractmethod
    def base_name(self):
        raise Exception()


class Engineer(Person):

    def base_name(self):
        return "Engineer"
    pass


class Technician(Person):

    def base_name(self):
        return "Technician"

    pass


class Barber(Person):

    def base_name(self):
        return "Barber"

    pass


class Politician(Person):

    def base_name(self):
        return "Politician"

    pass






