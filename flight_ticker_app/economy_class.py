#     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#
#                             ECONOMY CLASS
#
#     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
import general
import rand

# -------- function ----------------------------------------------------------------------------------------------------


# The function asks the user to insert the chair he has chosen, checks the input and returns the chair's letter
def chair_choose() -> str:
    while True:
        chair_ = input("Please enter the letter of the chair you choose: ").strip().lower()
        if chair_ in ('a', 'b', 'c', 'd', 'e', 'f'):
            return chair_.upper()
        else:
            print("\n\033[4;1;31mPlease enter one of the letters A, B, C, D, E, F\033[1;0m")


# The function checks if the chair is near the window and returns where the chair is located and the price
def window_or_not(chair_s: str):
    chair_s = chair_s.lower()
    extra_w = 10
    if chair_s in ('a', 'f'):
        return 'window', extra_w
    elif chair_s in ('c', 'd'):
        extra_w = 0
        return 'aisle', extra_w
    else:
        extra_w = 0
        return 'middle', extra_w


def line_choose():
    extra_leg_line = (12, 22, 42)
    extra_leg = 15

    while True:
        line_ = input("\nPlease enter the line number you want 11-60: ").strip().lower()

        if line_.isdigit():
            line_ = int(line_)

            if line_ in range(11, 61):
                price_ = line_price(line_)

                if line_ in extra_leg_line:
                    return line_, price_, extra_leg
                else:
                    extra_leg = 0
                    return line_, price_, extra_leg

            else:
                print("\n\033[4;1;31myou are out of range. Please enter in range 11-60\033[1;0m")
        else:
            print("\n\033[4;1;31mPlease enter a number in range 11-60\033[1;0m")


def line_price(line_selection):
    price_11_20 = 1700
    price_21_40 = 1500
    price_41_60 = 1200

    if line_selection in range(11, 21):
        return price_11_20

    elif line_selection in range(21, 41):
        return price_21_40
    else:
        return price_41_60


# The function receives from the user the meal he chooses.
# Returns the name of the meal and the additional payment, if any
def meal_pre(menu_, a, b) -> tuple[str, int]:
    busi = 22
    lux = 42
    Econo = 7
    menu_question = "Which meal do you prefer?"
    print("\n")
    print(menu_question.center(72))
    print(f"""     
                    |      1      |      2        |      3       |
                    | LUXURY MEAL | BUSINESS MEAL | ECONOMY MEAL |
                    |     {a}+24{b}     |     {a}+22{b}       |     {a}+7{b}       |

        \033[1;1;36mLuxury menu:\033[1;0m
        {menu_['menu1']} 
        {menu_['menu2']} 
        {menu_['menu3']}          
                 """)
    while True:
        meal_p = input("Enter 1 - Luxury meal, 2 - Business meal, 3 - Economy meal: ").strip()
        if meal_p.isdigit():
            meal_p = int(meal_p)
            if meal_p == 1:
                return 'Luxury meal', lux
            elif meal_p == 2:
                return 'Business meal', busi
            elif meal_p == 3:
                return 'Economy meal', Econo
            else:
                print("\n\033[4;1;31mPlease enter 1, 2 or 3\033[1;0m")
        else:
            print("\n\033[4;1;31mPlease enter a number\033[1;0m")


# The function receives from the user the weight of his luggage.
# returns the weight and how much he needs to add, if any
def luggage_check():
    while True:
        lug_max = 20
        lug_weight = input("\nWhat is your luggage weight? \n($10/kg if exceeds 20kg)")
        if lug_weight.isdigit():
            lug_weight = int(lug_weight)
            if 0 < lug_weight <= lug_max:
                extra_lug = 0
                return lug_weight, extra_lug
            else:
                extra_lug = (lug_weight - lug_max) * 10
                return lug_weight, extra_lug
        else:
            print("\n\033[4;1;31mPlease enter a number, cant be - 0\033[1;0m")


# -------- function ----------------------------------------------------------------------------------------------------


#  ------------ main business class function -----------------------------------------------------------------

def main_economy_class(name, last_name, menu):

    # blue color
    a = '\033[1;1;36m'

    # regular color
    b = '\033[1;0m'

    print("\n\n\n")
    print("""
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXXX ECONOMY CLASS XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        """)
    print(f"""
             ================================================================
                          Our seats                   |  Luggage                     
                                                      |  {a}$10/kg if exceeds 20kg{b}
                   {a}+$10   +0         +0   +$10{b}        |  
              window | [A][B][C]  [D][E][F] | window  |  line : 11-20 - {a}$1,700{b}
                   {a}+$10   +0         +0   +$10{b}        |  
              window | [A][B][C]  [D][E][F] | window  |  line : 21-40 - {a}$1,500{b} 
                   {a}+$10   +0         +0   +$10{b}        |  
              window | [A][B][C]  [D][E][F] | window  |  line : 41-60 - {a}$1,200{b}    
                                                      |
                        Economy meal: {a}+$7{b}             |  Luxury meal: {a}+$42{b} 
              Extra leg room - line 12,22,42: {a}+$15{b}    |  Business meal: {a}+$22{b}
             ================================================================
            """)

    chair: str = chair_choose()

    line, price, extra_leg_room = line_choose()

    place_chair, extra_window = window_or_not(chair)

    meal, extra_meal = meal_pre(menu,a ,b)

    luggage, extra_luggage = luggage_check()

    meal_preference: str = general.kosher_or_not()

    print("\n\n\n")
    print(f"""\033[1;1;37m
                                   Your flight ticket

            XXXXXXXXXXXXXXXXXXXXXXXXX ECONOMY CLASS XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

            ======================= TEL AVIV - NEW YORK ===========================\033[1;0m

              PASSENGER: {a}{name} {last_name}{b}     FLIGHT: {a}STA-055{b}      DATE: {a}10 MAR 2023{b}

              SEAT: {a}{line}{chair}-{place_chair}{b}         MEAL PREFERENCE: {a}{meal_preference}{b}

              LUGGAGE: {a}{luggage}kg{b}          MEAL: {a}{meal}{b}

            ======================================================================= """)

    extra_print = f"Extra window: ${extra_window}, Extra meal: ${extra_meal}, Extra luggage: ${extra_luggage}, " \
                  f"Extra room for the legs: ${extra_leg_room}"
    extra = extra_window + extra_meal + extra_luggage + extra_leg_room

    final = price + extra
    final_print = f"The final price: {a}${final}{b}    extras: {a}${extra}{b}"

    print(extra_print.center(100))
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
# main_economy_class('yael', 'ben', menu)