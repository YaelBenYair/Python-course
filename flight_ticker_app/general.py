import first_class
import business_class
import economy_class

# The function checks the user's meal preference and returns kosher or regular
def kosher_or_not() -> str:
    print("\nDo you want s Kosher meal?")
    while True:
        k_choose = input("Enter 1 - yes, 2- no: ")
        if k_choose.isdigit() and int(k_choose) == 1:
            return 'kosher'
        elif k_choose.isdigit() and int(k_choose) == 2:
            return 'regular'
        else:
            print("\n\033[4;1;31mPlease enter a number: 1 - for yes, 2 - for no\033[1;0m")


# The function asks the user to enter his name and returns the name after checking that it is
# correct and there are no numbers
def name_enter_check(masseg) ->str:
    while True:
        name_user = input(f"Please enter your {masseg}: ").strip()
        if name_user.isalpha():
            return name_user
        elif " " in name_user or "-" in name_user:
            name = name_user.split(" ")
            name = "".join(name)
            name = name.split(" ")
            name = "".join(name)

            if name.isalpha():
                return name_user
            else:
                print("\n\033[4;1;31mPlease enter only letters\033[1;0m")
        else:
            print("\n\033[4;1;31mPlease enter only letters\n\033[1;0m")


# The function checks the number the user selected
def number_of_class_check() ->int:
    while True:
        class_choose_num = input("Which class do you choose? Please enter the class number: ").strip()
        if class_choose_num.isdigit() and 1 <= int(class_choose_num) <= 3:
            return int(class_choose_num)
        else:
            print("\n\033[4;1;31mPlease enter a number. 1 - first class, 2 - business class, 3 - economy class\n\033[1;0m")


# The function receives the first and last name, asks the user to select the class he wants,
# and then sends the details to the functions of the class the user selected
def choose_your_class(user_name, user_last_name, menu):
    msn = "These are the classes we have"
    print("\n")
    print(msn.center(72))
    print("""     
             |      1      |       2        |       3       |
             | FIRST CLASS | BUSINESS CLASS | ECONOMY CLASS |
             |             |                |               | 
             """)

    class_choose = number_of_class_check()
    # sending for first class function
    if class_choose == 1:
        first_class.main_first_class(user_name, user_last_name, menu)

    # sending for business class function
    elif class_choose == 2:
        business_class.main_business_class(user_name, user_last_name, menu)

    # sending for economy class function
    else:
        economy_class.main_economy_class(user_name, user_last_name, menu)






