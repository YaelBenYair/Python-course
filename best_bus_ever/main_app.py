import os
import pickle
from best_bus_comp import BestBusCompany
from BestBusCompanyExceptions import *
from passenger_menu_func import *
from manager_menu_func import *


def main_menu(func: Callable, msg: str, num_range: int):
    while True:
        try:
            func()
            menu_selection: int = selection(msg, num_range)
            break
        except ValueError:
            print("\nThe input must be a number\n")
        except BestBusCompanyExceptions as e:
            print(e)

    return menu_selection

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
            selection_user = selection("[1] - Manager\n[2] - Passenger\nEnter 1,2: ", 2)
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

            menu_select = main_menu(display_menu, "Enter your selection 1-6: ", 6)

            match menu_select:
                case 1:
                    add_route(bus_company)

                case 2:
                    delete_route(bus_company)

                case 3:
                    update_route(bus_company)

                case 4:
                    add_scheduled_ride(bus_company)

                case 5:
                    print(bus_company.get_lins_by_num())

                case 6:
                    exit_func = True

    elif selection_user == 2:
        exit_func = False

        while not exit_func:
            menu_select = main_menu(display_menu_passenger, "Enter your selection 1-3: ", 3)

            match menu_select:
                case 1:
                    search_route(bus_company)

                case 2:
                    report_delay(bus_company)

                case 3:
                    exit_func = True
    print("Bye bye")

    # before exiting the program, persist the current state
    # of te system in the file, so next time it will be loaded
    with open('db\\bus_company.pickle', 'wb') as fh:
        pickle.dump(bus_company, fh)















