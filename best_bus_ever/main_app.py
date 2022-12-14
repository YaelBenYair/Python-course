import os
import pickle
from best_bus_ever.best_bus_comp import BestBusCompany
from BestBusCompanyExceptions import *


# def manager_passenger(msg: str, maxi: int) -> int:
#     while True:
#         selection = int(input("Enter 1 - for manager, 2 - for passenger: "))
#         if selection < 1 or selection > 2:
#             raise OutOfRangeError(selection)
#         return selection
#
# def menu_selection() -> int:
#     while True:
#         selection = int(input("Enter your selection 1-5: "))
#         if selection < 1 or selection > 5:
#             raise OutOfRangeError(selection)
#         return selection

def selection(msg: str, maxi: int) -> int:
    while True:
        selection = int(input(msg))
        if selection < 1 or selection > maxi:
            raise OutOfRangeError(selection)
        return selection


def password_check() -> bool:
    pas = None
    count = 1
    equal = False
    # check password
    while not equal and count <= 3:
        pas = input("Please enter a password: ").strip()
        count += 1
        if pas == password:
            equal = True
        elif not equal and count < 3:
            print("\nIncorrect password! please try again\n")
    return equal


def display_menu():
    print("\nHello Manager!\nWhat actions would you like to take?\n"
          "1 - Add route\n"
          "2 - Delete route\n"
          "3 - Update route\n"
          "4 - Add scheduled ride\n"
          "5 - Exit\n")


def insert_origin_destin(msg) -> str:
    while True:
        stop_in = input(msg).strip()
        stop = "".join(stop_in.split(" "))
        if stop.isalpha():
            return stop_in
        raise StringEror()


def insert_stops():
    stops = input("Please enter line stops in format - A,B,C,D: ")
    for char in stops:
        if char.isalpha() or char in (" ", ",", "-"):
            continue
        else:
            raise FormatError()
    return stops


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    password = "RideWithUs!"

    # check whether this is the first time you run the app
    # if this is the first time - create a new class
    if not os.path.exists('db\\bus_company.pickle'):
        bus_company = BestBusCompany()
    else:
        # this is not the first time - we already have a DB
        # with data from the previous runs
        with open('db\\bus_company.pickle', 'rb') as fh:
            bus_company = pickle.load(fh)

    print("Welcome to Best Bus Company!\nare you manager or passenger")

    # check input manager or passenger
    while True:
        try:
            selection_user = selection("Enter 1 - for manager, 2 - for passenger: ", 2)
            break
        except ValueError:
            print("\nThe input must be a number\n")
        except BestBusCompanyExceptions as e:
            print(e)

    # if manager
    if selection_user == 1:
        if password_check():
            exit_func = False
            # print("hello")
        else:
            exit_func = True
            # print("bye bye")

        while not exit_func:
            while True:
                try:
                    display_menu()
                    menu: int = selection("Enter your selection 1-5: ", 5)
                    break
                except ValueError:
                    print("\nThe input must be a number\n")
                except BestBusCompanyExceptions as e:
                    print(e)

            match menu:
                case 1:
                    # case 1 - add route
                    while True:
                        try:
                            lin_num = int(input("Please enter line number: "))
                            origin = insert_origin_destin("Please enter origin: ")
                            destin = insert_origin_destin("Please enter destination: ")

                            while True:
                                try:
                                    bus_stops = insert_stops()
                                    break
                                except ValueError:
                                    print("\nThe input must be a string\n")
                                except BestBusCompanyExceptions as e:
                                    print(e)
                            # Creates a bus variable only if all inputs are true
                            bus_company.add_route(lin_num, origin, destin, bus_stops)
                            break
                        except ValueError:
                            print("\nThe input must be a number\n")
                        except BestBusCompanyExceptions as e:
                            print(e)

                case 2:
                    print('delete_route()')
                case 3:
                    print('update_route()')
                case 4:
                    print('add_scheduled_ride()')
                case 5:
                    exit_func = True
    print(bus_company.get_lins_by_num())



    # if manager or passenger
    # manager:
    # while < 3 - password = RideWithUs!
    # exit = False
    # while not exit
    # input(menu)
    # match menu:
    # case 1:
    #     add_route()
    # case 2:
    #     delete_route()
    # case 3:
    #     update_route()
    # case  4:
    #     add_scheduled_ride()
    # case 5:
    #     exit = True
    # loop until exit

    # passenger:
    # exit = False
    # while not exit
    # input(menu)
    # match menu:
    # case 1:
    #     search_route
    # case 2:
    #     report_delay
    # case 3:
    #     exit = True
    # loop until exit

        # before exiting the program, persist the current state
        # of te system in the file, so next time it will be loaded
    with open('db\\bus_company.pickle', 'wb') as fh:
        pickle.dump(bus_company, fh)


# print(bus_c.add_route(16, 'Tayasim', 'Opera', 'school,park,sea,xxx'))















