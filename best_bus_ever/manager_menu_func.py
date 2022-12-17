from general_func import *
import datetime
from BestBusCompanyExceptions import *
from typing import Callable


def display_menu():
    print("\nHello Manager!\nWhat actions would you like to take?\n"
          "[1] - Add route\n"
          "[2] - Delete route\n"
          "[3] - Update route\n"
          "[4] - Add scheduled ride\n"
          "[5] - Display route\n"
          "[6] - Exit\n")


def display_menu_update():
    print("\nWhat updates would you like to do?\n"
          "[1] - Origin\n"
          "[2] - Destination\n"
          "[3] - Stops\n"
          "[4] - Exit\n")


def password_check() -> bool:
    password = "RideWithUs!"
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


def time_check(msg):
    while True:
        try:
            t_insert_time = input(msg)
            if t_insert_time.count(":") > 1 or t_insert_time.count(":") == 0:
                raise FormatError()

            t_insert_time = t_insert_time.split(":")
            de_time = datetime.time(int(t_insert_time[0]), int(t_insert_time[1]))
            de_time = de_time.strftime("%H:%M")
            break
        except ValueError as e:
            print(e)
    return de_time


def check_insert_stops():
    stops = input("Please enter line stops in format - A,B,C,D: ")
    for char in stops:
        if char.isalpha() or char in (" ", ",", "-"):
            continue
        else:
            raise FormatError()
    return stops.title()

def insert_bus_stops():
    while True:
        try:
            bus_stops = check_insert_stops()
            break
        except ValueError:
            print("\nThe input must be a string\n")
        except BestBusCompanyExceptions as e:
            print(e)
    return bus_stops


def update_origin_destin(msg: str, num: int, func: Callable):
    while True:
        try:
            origin_destin = insert_origin_destin(msg)
            func(num, origin_destin)
            print("The update added successfully!")
            break
        except BestBusCompanyExceptions as e:
            print(e)


def add_route(bus_company):
    while True:
        try:
            lin_num = int(input("Please enter line number: "))
            origin = insert_origin_destin("Please enter origin: ").strip().capitalize()
            destin = insert_origin_destin("Please enter destination: ").strip().capitalize()
            bus_stop = insert_bus_stops()

            # Creates a bus variable only if all inputs are true
            bus_company.add_route(lin_num, origin, destin, bus_stop)
            print("The line has been successfully added")
            break
        except ValueError:
            print("\nThe input must be a number\n")
        except BestBusCompanyExceptions as e:
            print(e)


def delete_route(bus_company):
    while True:
        try:
            lin_num = int(input("Please enter the line number you want to delete: "))
            yes_no = selection(f"Are you sure you want to delete line number {lin_num}?\n"
                               f"[1] - yes\n[2] - no", 2)
            if yes_no == 1:
                bus_company.delete_route(lin_num)
                print("The line has been successfully deleted")
            break
        except ValueError:
            print("\nThe input must be a number\n")
        except BestBusCompanyExceptions as e:
            print(e)


def update_route(bus_company):
    while True:
        try:
            lin_num = int(input("Please enter the line number you want to update: "))
            bus_company.display_information_route_by_line(lin_num)
            while True:
                try:
                    display_menu_update()
                    menu_update: int = selection("Enter your selection 1-4: ", 4)

                    match menu_update:
                        case 1:
                            update_origin_destin("Please enter new origin: ", lin_num, bus_company.update_origin)

                        case 2:
                            update_origin_destin("Please enter new destination: ", lin_num, bus_company.update_destin)
                        case 3:
                            bus_stop = insert_bus_stops()
                            bus_company.update_stops(lin_num, bus_stop)
                        case 4:
                            pass
                    break
                except ValueError:
                    print("\nThe input must be a number\n")
                except BestBusCompanyExceptions as e:
                    print(e)

            break
        except ValueError:
            print("\nThe input must be a number\n")
        except BestBusCompanyExceptions as e:
            print(e)


def add_scheduled_ride(bus_company):
    while True:
        try:
            lin_num = int(input("Please enter the line number you want to update: "))
            bus_company.get_scheduled_line(lin_num)
            origin_time = time_check("Please enter the origin time in format HH:MM: ")
            destin_time = time_check("Please enter the destination time in format HH:MM: ")
            driver_name = insert_origin_destin("Enter driver name: ")
            bus_company.add_scheduled(lin_num, origin_time, destin_time, driver_name)
            print("The scheduled added successfully!")
            break
        except ValueError:
            print("\nThe input must be a number\n")
        except BestBusCompanyExceptions as e:
            print(e)













