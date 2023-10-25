import random

class bankAccount:
    def __init__(self, name):
        self.name = name
        self.account_number = self.generate_account_number()
        self.balance = 0

