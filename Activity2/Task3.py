class Ba:
    
    def __init__(self, an, o, b=0):
        self.an = an
        self.o = o
        self.b = b

    def deposit(self, am):
        am = int(input("Enter Deposit: "))
        self.b += am
        print(f"Deposited ${am}. New balance: ${self.b}")

    def withdraw(self, am):
        am = int(input("Enter Withdrawal: "))
        nb = self.b - am
        print(f"Withdrew ${am}. New balance: ${nb}")

    def display_balance(self):
        print(f"Account balance for {self.o}: ${self.b}")


acc = Ba("09947393341", "Fabi", 0)

acc.deposit(0)
acc.withdraw(0)
acc.display_balance()
