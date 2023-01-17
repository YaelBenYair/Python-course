import argparse
from transfer_request_db import Bank

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
            prog='transfer action in bank',
            description='The program allows you to transfer between accounts\n'
                        'num_account1 | required | account number of the sender\n'
                        'num_account2 | required | account number of the receiver\n'
                        'customer_passport | required | the id number of the sender\n'
                        'amunt | required | amount of the transfer\n',
            epilog='Text at the bottom of help')

    parser.add_argument('num_account1', type=int, help="transfer sender account number")
    parser.add_argument('num_account2', type=int, help="transfer receiver account number")
    parser.add_argument('customer_passport', type=int, help="transfer sender id number")
    parser.add_argument('amunt', type=int, help="amount of the transfer")

    args = parser.parse_args()
    transfer = Bank()
    transfer.run(args.num_account1, args.num_account2, args.customer_passport, args.amunt)




# def run(self, count1: int, count2: int, customer_passport: int, amunt: int):
# b.run(123, 456, 153462, 10000)

