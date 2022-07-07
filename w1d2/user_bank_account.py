class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        if self.balance<amount:
            print('insufficient funds')
            self.balance = self.balance - 5
            return self
        self.balance = self.balance - amount
        return self

    def display_account_info(self):
        print(f"Balance:${self.balance}")
        return self



    def yield_interest(self):
        self.balance = self.balance + self.balance*self.int_rate
        return self

my_bankAccount = BankAccount(.1, 100)
my_bankAccount2 = BankAccount(.1,200)

my_bankAccount.deposit(50).deposit(50).deposit(50).withdraw(50).display_account_info().yield_interest().display_account_info()
my_bankAccount2.deposit(100).deposit(5000).withdraw(100).withdraw(200).withdraw(100).yield_interest().display_account_info()