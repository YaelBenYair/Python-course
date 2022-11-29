#     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#
#                             BUSINESS CLASS
#
#     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
import first_class
import general
import rand

# -------- function ----------------------------------------------------------------------------------------------------


# The function asks the user to enter the line number, checks the input and returns the line number and the price
def line_choose() -> tuple[int, int]:
    price_3000 = (5, 6, 7)
    price_2300 = (8, 9, 10)
    while True:
        line_ = input("\nPlease enter the line number you want 5-10: ").strip().lower()
        if line_.isdigit():
            if int(line_) in price_3000:
                price_ = 3000
                return (int(line_), price_)
            elif int(line_) in price_2300:
                price_ = 2300
                return (int(line_), price_)
            else:
                print("\n\033[4;1;31myou are out of range. Please enter in range 5-10\033[1;0m")
        else:
            print("\n\033[4;1;31mPlease enter a number in range 5-10\033[1;0m")


# The function checks if the chair is near the window and returns where the chair is located and the price
def window_or_not(chair_s: str):
    chair_s = chair_s.lower()
    extra_w = 55
    if chair_s in ('a', 'd'):
        return 'window', extra_w
    else:
        extra_w = 0
        return 'aisle', extra_w


# The function receives from the user the weight of his luggage.
# returns the weight and how much he needs to add, if any
def luggage_check():
    while True:
        lug_weight = input("\nWhat is your luggage weight? \n($10/kg if exceeds 50kg)")
        if lug_weight.isdigit():
            lug_weight = int(lug_weight)
            if 0 < lug_weight <= 50:
                extra_lug = 0
                return lug_weight, extra_lug
            else:
                extra_lug = (lug_weight - 50) * 10
                return lug_weight, extra_lug
        else:
            print("\n\033[4;1;31mPlease enter a number, cant be - 0\033[1;0m")


# The function receives from the user the meal he chooses.
# Returns the name of the meal and the additional payment, if any
def meal_pre(menu_, a, b) -> tuple[str, int]:
    busi = 0
    lux = 42
    menu_question = "Which meal do you prefer?"
    print("\n")
    print(menu_question.center(72))
    print(f"""     
                    |      1        |      2      |   
                    | BUSINESS MEAL | LUXURY MEAL |
                    |               |     {a}+42{b}     | 
                 
        {a}Luxury menu:{b}
        {menu_['menu1']} 
        {menu_['menu2']} 
        {menu_['menu3']}          
                 """)
    while True:
        meal_p = input("Enter 1 - Business meal, 2 - Luxury meal: ").strip()

        if meal_p.isdigit():
            meal_p = int(meal_p)

            if meal_p == 1:
                return 'Business meal', busi

            elif meal_p == 2:
                return 'Luxury meal', lux

            else:
                print("\n\033[4;1;31mPlease enter 1 or 2\033[1;0m")
        else:
            print("\n\033[4;1;31mPlease enter a number\033[1;0m")

# -------- function ----------------------------------------------------------------------------------------------------


#  ------------ main business class function -----------------------------------------------------------------

def main_business_class(name, last_name, menu):
    # blue color
    a = '\033[1;1;36m'

    # regular color
    b = '\033[1;0m'

    print("\n\n\n")
    print("""
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXX BUSINESS CLASS XXXXXXXXXXXXXXXXXXXXXXXXXX
        """)
    print(f"""
         ================================================================
                      Our seats                |  Luggage                     
                                               |  {a}$10/kg if exceeds 50kg{b}
               {a}+$55     +0  +0     +$55{b}        |  
          window | [A]  [B] [C]  [D] | window  |  line : 5-7  - {a}$3,000{b}
               {a}+$55     +0  +0     +$55{b}        |  
          window | [A]  [B] [C]  [D] | window  |  line : 8-10 - $2,300 
                                               |   
                                               |  Luxury meal: {a}+$42{b}
         ================================================================
        """)

    chair: str = first_class.chair_choose()

    line, price = line_choose()

    place_chair, extra_window = window_or_not(chair)

    meal, extra_meal = meal_pre(menu, a, b)

    luggage, extra_luggage = luggage_check()

    meal_preference: str = general.kosher_or_not()

    print("\n\n\n")
    print(f"""\033[1;1;37m
                                Your flight ticket

        XXXXXXXXXXXXXXXXXXXXXXXXX BUSINESS CLASS XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        ======================= TEL AVIV - NEW YORK ===========================\033[1;0m

          PASSENGER: {a}{name} {last_name}{b}     FLIGHT: {a}STA-055{b}      DATE: {a}10 MAR 2023{b}

          SEAT: {a}{line}{chair}-{place_chair}{b}         MEAL PREFERENCE: {a}{meal_preference}{b}

          LUGGAGE: {a}{luggage}kg{b}          MEAL: {a}{meal}{b}

        ======================================================================= """)

    extra_print = f"Extra window: ${extra_window}, Extra meal: ${extra_meal}, Extra luggage: ${extra_luggage}"
    extra = extra_window + extra_meal + extra_luggage

    final = price + extra
    final_print = f"The final price: {a}${final}{b}    extras: {a}${extra}{b}"

    print(extra_print.center(76))
    print(final_print.center(100))

    print("\n")

    rand_num = rand.discount(name, last_name)
    rand.check_rand_num(rand_num, final)




# ----------------------------------------------------------------------------------------------------------------------
#
# menu = {
#         'menu1': 'STARTER - Roast veal sweetbread, MAIN - Cornish turbot,  DESERT - Hazelnut souffle ',
#
#         'menu2': 'STARTER - Ravioli lobster, MAIN - 100-Day aged Cumbrian Blue Grey, DESERT  - Pecan praline ',
#
#         'menu3': 'STARTER - Scallops from the Isle of Skye, MAIN - Aynhoe Park fallow deer, DESERT  - '
#                   'Caramelised apple Tarte Tatin'
#     }
#
# main_business_class('yael', 'ben', menu)
#
#



