# import rand
import sys, time, os
import general

# ---------- function ------------------------------------------------------------------------------------------------

# The function prints the string at the set rate
def typrun(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(0.02)
        else:
            time.sleep(0.2)

# ---------- function ------------------------------------------------------------------------------------------------

# ---------- main -----------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    menu = {
        'menu1': 'STARTER - Roast veal sweetbread, MAIN - Cornish turbot,  DESERT - Hazelnut souffle ',

        'menu2': 'STARTER - Ravioli lobster, MAIN - 100-Day aged Cumbrian Blue Grey, DESERT  - Pecan praline ',

        'menu3': 'STARTER - Scallops from the Isle of Skye, MAIN - Aynhoe Park fallow deer, '
                 'DESERT - Caramelised apple Tarte Tatin'
    }

    print("""\033[1;1;37m
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    
                      FLIGHT TICKET ORDER APP
    
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\033[1;0m""")

    welcome = "Welcome to the application for booking a flight ticket"
    welcome_from = "from Tel Aviv to New York"
    # print(f"{typrun(welcom)}")
    print(f"\033[1;1;34m{welcome.center(72)}\033[1;0m")
    print(f"\033[1;1;34m{welcome_from.center(72)}\033[1;0m", end=" ")

    print("""
    \033[1;1;34m-------------------------------------------------------------------\033[1;0m
    """)

    name = general.name_enter_check('name')
    last_name = general.name_enter_check('last name')

    print()

    general.choose_your_class(name, last_name, menu)



    # os.system("cls")  # = clear for Windows
    # os.system('clear')  # for Mac


















