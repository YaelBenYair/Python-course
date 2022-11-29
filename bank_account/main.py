from bank import Bank


if __name__ == '__main__':
    bank_account = Bank()
    bank_account.add_account(4285615, 'Mercantile', 'Yafo', 653, 5000, True, 'Reut Hash', 285437959)
    bank_account.add_account(5348956, 'Leumi', 'Givatayim', 856, 8000, False, 'Itsik Ben', 203663810)
    bank_account.add_account(5348956, 'Leumi', 'Givatayim', 856, 8000, False, 'Yael Ben', 308019272)

    bank_account.display_account_holders()

    bank_account.display_account_numbers()

    bank_account.display_branch_accounts()

    bank_account.add_cash(308019272, 300)
    bank_account.display_account_status(308019272)
    bank_account.add_cash(308019272, 4000)
    bank_account.display_account_status(308019272)

    bank_account.display_transactions_per_date(308019272)