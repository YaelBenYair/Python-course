from account_details_and_holder import AccountHolder, AccountDetails
import datetime

class Bank:
    def __init__(self):
        self.branch_account: {str: list} = {}
        self.account_holders: {int: AccountDetails} = {}
        self.account_numbers: {int: list[AccountHolder]} = {}
#

    def add_account(self, account_number: int, bank_name: str, bank_branch_name: str,
                    bank_branch_number: int, maximum_credit_limit: int, usd_allowes: bool,
                    name: str, person_id: int, address: str = None,
                    maile: str = None, money_in: float = 0):

        if person_id in self.account_holders:
            print("This name is already exists!")
            return None
        # add holder and his account
        holder = AccountHolder(name, person_id, address, maile)
        account = AccountDetails(account_number, bank_name, bank_branch_name, bank_branch_number,
                                 maximum_credit_limit, usd_allowes , money_in)

        # List by name holder
        self.account_holders[person_id] = account

        if account_number not in self.account_numbers:
            self.account_numbers[account_number] = []
        self.account_numbers[account_number].append(holder)

        if bank_name not in self.branch_account:
            self.branch_account[bank_name] = []
        self.branch_account[bank_name].append([account, holder])

        print("The account has been successfully added\n")

    def display_account_holders(self):
        print("List by Id")
        count = 0
        account_num = None

        # Orderly printing of the data
        for holder in self.account_holders:

            # Search and print the name of the account holder
            num = self.account_holders[holder].account_number

            if num == account_num:
                count += 1
            account_num = num
            name = self.account_numbers[num][count].name
            print(f"{holder}-{name}: {self.account_holders[holder]}\n")

    def display_account_numbers(self):
        print("List by account numbers")
        for num in self.account_numbers:
            print(f"{num}: {self.account_numbers[num]}\n")

    def display_branch_accounts(self):
        print("List by branch names")
        for branch in self.branch_account:
            print(f"{branch}: {self.branch_account[branch]}\n")

    # The function prints the account balance status
    def display_account_status(self, id: int):
        if id in self.account_holders:
            print(f"Your account balance: {self.account_holders[id].account_balance}")

    def display_transactions_per_date(self, id: int):
        if id in self.account_holders:
            print("All transactions by date")
            print(self.account_holders[id].transactions_per_date)

    # The function adds money to the account
    def add_cash(self, id: int, amount: float):
        if id in self.account_holders:
            self.account_holders[id].add_cash(amount, f"{amount} NIS were added to the account")

    # The function sends to a conversion function
    def usd_convert(self, id: int, amount_convert: float):
        if id in self.account_holders:
            self.account_holders[id].usd_convert(amount_convert, "The shekel to dollar conversion has been made")

    # The function transfers between accounts
    def account_transfer(self, name_holder, holder_id: int, transfer_amount: float, other_name, other_id: int,
                         other_bank_name: str, other_branch_number: int, other_account_num: int):

        # Checking if both people exist in the dict
        if holder_id in self.account_holders and other_id in self.account_holders and transfer_amount > 0:
            name = self.account_holders[other_id]

            # Verification of account details
            if other_branch_number == name.bank_branch_number and other_bank_name == name.bank_name \
                    and other_account_num == name.account_number:
                self.account_holders[holder_id].withdraw_cash(transfer_amount, f"{transfer_amount} NIS was "
                                                                               f"successfully transferred to "
                                                                               f"{other_name}")
                self.account_holders[other_id].add_cash(transfer_amount,f"{transfer_amount}NIS was transferred "
                                                                        f"to your account from {name_holder}")
            else:
                print("Bank account details are incorrect")
                return None
        else:
            print("The account does not exist")
            return None