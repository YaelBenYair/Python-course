from moria.maman_13.class_run_time.class_parent import *

input_msg = {
    'name_class': "Please enter the name of new class:\n",
    'menu_base_class': "\nPlease enter name of base class (blank if none):\n"
                       "[1] - Engineer\n"
                       "[2] - Technician\n"
                       "[3] - Barber\n"
                       "[4] - Politician\n",
    'attribute': "Please enter name of new attribute for class Student:\n"
}


def display_name_class():
    print("Please enter the name of new class:\n")


def display_menu_base_class():
    print("\nPlease enter name of base class (blank if none):\n"
          "[1] - Engineer\n"
          "[2] - Technician\n"
          "[3] - Barber\n"
          "[4] - Politician\n")


def display_attribute():
    print("Please enter name of new attribute for class Student:\n")


def check_input_str(user_input: str) -> str:
    if isinstance(user_input, str):
        return user_input.title()
    raise Exception()


def check_input_int(user_input: int | str, can_be_none: bool, max_range: int) -> int | None:
    if can_be_none:
        if user_input == '':
            return None
    if user_input.isdigit() and 1 <= int(user_input) <= max_range:
        return int(user_input)
    raise Exception()


class Menu:

    def __init__(self):
        self.cls_instance = None
        self.attribute = None
        self.base_class = None
        self.class_name = None

    def run(self):
        self.class_name: str = check_input_str(input(input_msg['name_class']).strip())

        self.base_class: int = check_input_int(input(input_msg['menu_base_class']), True, 4)

        self.attribute = input(input_msg['attribute'])

        match self.base_class:
            case 1:
                self.cls_instance = type(self.class_name, (Engineer,), {self.attribute: None})
            case 2:
                self.cls_instance = type(self.class_name, (Technician,), {self.attribute: None})
            case 3:
                self.cls_instance = type(self.class_name, (Barber,), {self.attribute: None})
            case 4:
                self.cls_instance = type(self.class_name, (Politician,), {self.attribute: None})
            case None:
                self.cls_instance = type(self.class_name, (), {self.attribute: None})
            case _:
                raise Exception()

        instance = self.cls_instance()

        print(f"\nClass Student created with base class: {instance.base_name() if self.base_class else None}")
        print(f"Class __name__ is: {instance.display() if self.base_class else self.cls_instance.__name__}")
        print(f"Class __dict__ is: {self.cls_instance.__dict__}")

        pass

    pass
