class Bank:
    def __init__(self, an, o, b=0):
        self.an = an
        self._o = o
        self.__b = b

    def deposit(self, am):
        self.__b += am
        print(f"Deposited ${am}. New balance: ${self.__b}")

    def withdraw(self, am):
        self.__b -= am
        print(f"Withdrew ${am}. New balance: ${self.__b}")

    def display_balance(self):
        print(f"Account balance for {self._o}: ${self.__b}")

class acc(Bank):
    def display_owner(self):
        print(self._o)

acc1 = Bank("09947393341", "Fabi", 0)
acc2 = Bank("09909878876", "Yohai", 0)

acc1.display_balance()

dpst_amt = int(input("Enter Deposit Amount: "))
acc1.deposit(dpst_amt) 
wtdrl_amt = int(input("Enter Withdrawal Amount: "))
acc1.withdraw(wtdrl_amt) 

acc1.display_balance()