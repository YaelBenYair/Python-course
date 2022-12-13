import os
import pickle



if __name__ == '__main__':

    # check whether this is the first time you run the app
    # if this is the first time - create a new class
    if not os.path.exists('bus_company.pickle'):
        pass
        # bus_company = BestBusCompany()
    else:
        # this is not the first time - we already have a DB
        # with data from the previous runs
        with open('bus_company.pickle', 'rb') as fh:
            pass
            # bus_company = pickle.load(fh)

    # input manager or passenger
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
    with open('bus_company.pickle', 'wb') as fh:
        pass
        # pickle.dump(bus_company, fh)


















