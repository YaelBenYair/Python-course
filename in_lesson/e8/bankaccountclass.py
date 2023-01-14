import datetime
import threading

from readerwriterlock import rwlock


class BankAccount:
    def __init__(self, bank_num: int, bank_name: str):
        self.bank_num = bank_num
        self.bank_name = bank_name
        self.balance = 0
        self.transactions = []
        # self.rw_lock = rwlock.RWLockFairD()
        # self.r_lock = self.rw_lock.gen_rlock()
        # self.w_lock = self.rw_lock.gen_wlock()
        self.lock = threading.Lock()

    @staticmethod
    def is_number_positiv(num):
        if num < 0:
            raise Exception

    def deposit(self, amnt: int):
        self.is_number_positiv(amnt)
        # with self.w_lock:
        with self.lock:
            self.balance += amnt
            self.transactions.append(f"deposit {amnt}{datetime.datetime.now().date()}")

    def withdraw(self, amnt: int):
        self.is_number_positiv(amnt)
        # with self.w_lock:
        with self.lock:
            if self.balance >= amnt:
                self.balance -= amnt
                self.transactions.append(f"withdraw {amnt}{datetime.datetime.now().date()}")
            else:
                raise Exception()

    def get_balance(self):
        # with self.r_lock:
        return self.balance










































