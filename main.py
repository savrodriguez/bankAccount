import random

class bankAccount:
    def __init__(self, name):
        self.name = name
        self.account_number = self.generate_account_number()
        self.balance = 0

# Generate Account Number
def generate_account_number(self):
    return str(random.randint(10000000, 99999999))