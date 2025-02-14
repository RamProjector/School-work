class Ba:
    def __init__(self, an, o, b=0):
        self.an = an
        self.o = o
        self.b = b

    def deposit(self, am):
        self.b += am
        print(f"Deposited ${am}. New balance: ${self.b}")

    def withdraw(self, am):
        self.b -= am
        print(f"Withdrew ${am}. New balance: ${self.b}")

    def display_balance(self):
        print(f"Account balance for {self.o}: ${self.b}")


acc = Ba("09947393341", "Fabi", 405999)

acc.deposit(6000)
acc.withdraw(000)
acc.display_balance()