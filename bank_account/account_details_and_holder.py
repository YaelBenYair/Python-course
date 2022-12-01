import datetime
import random



####################################################################################
#                             AccountHolder
####################################################################################

class AccountHolder:
    def __init__(self, name: str, person_id: int, address: str = None, maile: str = None):
        self.name = name
        self.id = person_id
        self.address = address
        self.maile = maile

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Id: {self.id}\n" \
               f"Address: {self.address}\n" \
               f"Maile: {self.maile}"

    def __repr__(self):
        return f"Name: {self.name}\n" \
               f"Id: {self.id}"


####################################################################################
#                             AccountDetails
####################################################################################

class AccountDetails:
    def __init__(self, account_number: int, bank_name: str, bank_branch_name: str,
                 bank_branch_number: int, maximum_credit_limit: int = 0, usd_allowes: bool = False, money_in: float = 0, *usd_balance):
        # self.account_number = account_number
        today = datetime.date.today()
        
        self.account_number = random.randint(100000, 10000000)

        self.bank_name = bank_name
        self.bank_branch_name = bank_branch_name
        self.bank_branch_number = bank_branch_number
        self.maximum_credit_limit = maximum_credit_limit
        self.account_balance = money_in
        self.transactions_per_date: {str: list[str]} = {}
        self.current_date = f"{today.day}.{today.month}.{today.year}"

        self.usd_to_nis_rate = 3.16
        if usd_allowes:
            self.usd_balance = money_in / self.usd_to_nis_rate

    def __str__(self):
        return f"Account Number: {self.account_number}\n" \
               f"Account Balance: {self.account_balance}\n" \
               f"Bank Name: {self.bank_name}"

    def __repr__(self):
        return f"Account Number: {self.account_number}"

    def add_cash(self, amount, comment):
        self.current_date = f"{today.day}.{today.month}.{today.year}"

        if amount < 0:
            print("Cannot add a negative number")
            return None
        self.account_balance += amount

        # Adding an action to the account by date
        if self.current_date not in self.transactions_per_date:
            self.transactions_per_date[self.current_date] = []
        self.transactions_per_date[self.current_date].append(comment)
        print(comment)

    def withdraw_cash(self, amount_withdraw, comment):
        self.current_date = f"{today.day}.{today.month}.{today.year}"

        # Checks if it is possible to withdraw money
        if amount_withdraw > 0 and (self.account_balance - amount_withdraw) < (self.maximum_credit_limit * -1):
            self.account_balance -= amount_withdraw
        else:
            print(f"It is not possible to withdraw {amount_withdraw} NIS, exceeds the limit")
            return None

        # Adding an action to the account by date
        if self.current_date not in self.transactions_per_date:
            self.transactions_per_date[self.current_date] = []
        self.transactions_per_date[self.current_date].append(comment)
        print(comment)

    def usd_convert(self, amount_convert, comment):
        self.current_date = f"{today.day}.{today.month}.{today.year}"

        if amount_convert > 0:

            if self.current_date not in self.transactions_per_date:
                self.transactions_per_date[self.current_date] = []
            self.transactions_per_date[self.current_date].append(comment)
            print(comment)

            return amount_convert / self.usd_to_nis_rate
        else:
            print("Cannot convert a negative number")
            return None
