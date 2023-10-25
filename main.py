import random

class bankAccount:
    def __init__(self, name):
        self.name = name
        self.account_number = self.generate_account_number()
        self.balance = 0

    # Generate Account Number
    def generate_account_number(self):
        return str(random.randint(10000000, 99999999))


    # Deposits 
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Depositited: ${amount:.2f}")
        print(f"New Balance: ${self.balance:.2f}")

    #Withdrawl
    def withdrawl(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount:.2f}")
            print(f"New Balance: ${self.balance:.2f}")

        else: 
            print("Insufficient Funds")
            self.balance -= 10
            print(f"Overdraft fee of $10 has been charged!")

    # Getting Balance
    def getBalance(self):
        print(f"Balance: ${self.balance:.2f}")
        return self.balance

    # Print Statement
    def printStatement(self):
        print(f"{self.name}\nAccount No.: ****{self.account_number[-4:]}\nBalance: ${self.balance:.2f}")

    # Add Interest 
    def interest(self):
        interest = self.balance * 0.00083
        self.balance += interest


# TEST

savAccount = bankAccount("Savana")

savAccount.deposit(1500)
savAccount.printStatement()

savAccount.interest()
savAccount.printStatement()

savAccount.withdrawl(500)
savAccount.printStatement()


