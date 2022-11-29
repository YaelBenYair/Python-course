#     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#
#                                FIRST CLASS
#
#     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
from pprint import pprint
import general
import rand

# -------- function ----------------------------------------------------------------------------------------------------


# The function asks the user to insert the chair he has chosen, checks the input and returns the chair's letter
def chair_choose() -> str:
    while True:
        chair_ = input("Please enter the letter of the chair you choose: ").strip().lower()
        if chair_ in ('a', 'b', 'c', 'd'):
            return chair_.upper()
        else:
            print("\n\033[4;1;31mPlease enter one of the letters A, B, C, D\033[1;0m")


# The function asks the user to enter the line number, checks the input and returns the line number
def line_choose() -> int:
    while True:
        line_ = input("\nPlease enter the line number you want 1-4: ").strip().lower()
        if line_.isdigit() and int(line_) in (1, 2, 3, 4):
            return int(line_)
        else:
            print("\n\033[4;1;31mPlease enter a number in range 1-4\033[1;0m")


# The function checks if the chair is near the window and returns where the chair is located
def window_or_not(chair_s: str) -> str:
    chair_s = chair_s.lower()
    return 'window' if chair_s in ('a', 'd') else 'aisle'

# -------- function ----------------------------------------------------------------------------------------------------

#  ------------ main first class function -----------------------------------------------------------------

def main_first_class(name, last_name, menu):
    # blue color
    a = '\033[1;1;36m'

    # regular color
    b = '\033[1;0m'

    print("\n\n\n")
    print("""
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXXXX FIRST CLASS XXXXXXXXXXXXXXXXXXXXXXXXXXX
    """)
    print(f"""
        ======================================================
                     Our seats                |
                                              |  price: {a}$4,000{b}
         window | [A] [B] [C] [D] | window    |  line : 1 - 4
                                              |
        ======================================================
    """)

    chair: str = chair_choose()
    line: int = line_choose()
    place_chair: str = window_or_not(chair)
    price: int = 4000

    meal_preference: str = general.kosher_or_not()

    print("\n\n\n")
    print(f"""\033[1;1;37m
                           Your flight ticket
    
    XXXXXXXXXXXXXXXXXXXXXXXXXX FIRST CLASS XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    
    ======================= TEL AVIV - NEW YORK ===========================\033[1;0m 
                                                            
      PASSENGER: {a}{name} {last_name}{b}     FLIGHT: {a}STA-055{b}      DATE: {a}10 MAR 2023{b}                  
                                  
      SEAT: {a}{line}{chair}-{place_chair}{b}         MEAL PREFERENCE: {a}{meal_preference}{b}    
      
      LUGGAGE: {a}no additional fee{b}     MEAL: {a}Luxury, included in price{b}                   
     
    ======================================================================= """)

    final = f"The final price: {a}${price}{b}    extras: 0"
    print(final.center(80))

    print()

    print(f"You have 3 option meal:")
    pprint(menu)

    print("\n")

    rand_num = rand.discount(name, last_name)
    rand.check_rand_num(rand_num, price)







# ----------------------------------------------------------------------------------------------------------------------
# menu = {
#         'menu1': 'STARTER - Roast veal sweetbread, MAIN - Cornish turbot,  DESERT - Hazelnut souffle ',
#
#         'menu2': 'STARTER - Ravioli lobster, MAIN - 100-Day aged Cumbrian Blue Grey, DESERT  - Pecan praline ',
#
#         'menu3': 'STARTER - Scallops from the Isle of Skye, MAIN - Aynhoe Park fallow deer, DESERT  - '
#                   'Caramelised apple Tarte Tatin'
#     }
# main_first_class('yael', 'ben', menu)








