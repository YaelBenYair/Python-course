from BestBusCompanyExceptions import *
from general_func import *
import datetime
from BestBusCompanyExceptions import *
from typing import Callable

def display_menu_passenger():
    print("\nHello Passenger!\nWhat actions would you like to take?\n"
          "[1] - Search route\n"
          "[2] - Report delay\n"
          "[3] - Exit\n")


def search_route_menu():
    print("\nWhich way do you want to search?\n"
          "[1] - Line number\n"
          "[2] - Origin\n"
          "[3] - Destination\n"
          "[4] - Bus stops\n"
          "[5] - Exit\n")


def search_line_number(bus_company):
    while True:
        try:
            lin_num = int(input("Please enter the line number: "))
            print(bus_company.search_by_line(lin_num))
            break
        except ValueError:
            print("\nThe input must be a number\n")
        except BestBusCompanyExceptions as e:
            print(e)


def search_origin_destin(msg, func: callable):
    while True:
        try:
            origin_sear = insert_origin_destin(msg).capitalize()
            print(func(origin_sear))
            break
        except ValueError:
            print("\nThe input must be a string\n")
        except BestBusCompanyExceptions as e:
            print(e)


def search_stop(bus_company):
    while True:
        try:
            stop_sear = insert_origin_destin("Please insert stop you want to search: ").strip().capitalize()
            print(bus_company.search_by_bus_stop(stop_sear))
            break
        except ValueError:
            print("\nThe input must be a string\n")
        except BestBusCompanyExceptions as e:
            try:
                print(bus_company.search_by_destin(stop_sear))
                break
            except BestBusCompanyExceptions as e:
                try:
                    print(bus_company.search_by_origin(stop_sear))
                    break
                except BestBusCompanyExceptions as e:
                    print(e)



def search_route(bus_company):
    while True:
        try:
            search_route_menu()
            menu_search: int = selection("Enter your selection 1-5: ", 5)

            match menu_search:
                case 1:
                    search_line_number(bus_company)

                case 2:
                    search_origin_destin("Please insert origin you want to search: ", bus_company.search_by_origin)

                case 3:
                    search_origin_destin("Please insert destination you want to search: ", bus_company.search_by_destin)

                case 4:
                    search_stop(bus_company)

                case 5:
                    pass
            break
        except ValueError:
            print("\nThe input must be a number\n")
        except BestBusCompanyExceptions as e:
            print(e)


def report_delay(bus_company):
    search_route(bus_company)
    while True:
        try:
            lin_num = int(input("Please enter the line number you want to report: "))
            id_sche = int(input("Please enter scheduled id: "))
            bus_company.report_delay(lin_num, id_sche)
            break
        except ValueError:
            print("\nThe input must be a number\n")
        except BestBusCompanyExceptions as e:
            print(e)

















