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


acc = Ba("09947393341", "Fabi", 0)

acc.display_balance()

dpst_amt = int(input("Enter Deposit Amount: "))
acc.deposit(dpst_amt) 
wtdrl_amt = int(input("Enter Withdrawal Amount: "))
acc.withdraw(wtdrl_amt) 

acc.display_balance()
