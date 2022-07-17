class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance, balance2): 
        self.int_rate = int_rate
        self.balance = 0
        self.balance2 = 0
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount, account):
        if account == "Checking":
            self.balance+= amount
        elif account == "Savings":
            self.balance2+=amount
        return self
    def withdrawl(self, amount, account):
        if account == "Checking":
            if self.balance>= amount:
                self.balance -= amount
                return self
            else:
                print('insufficient funds')
                self.balance = self.balance - 5
                return self
        if account == "Savings":
            if self.balance2>= amount:
                self.balance2 -= amount
                return self
            else:
                print('insufficient funds')
                self.balance2 = self.balance2 - 5
                return self


    def display_account_info(self):
        print(f"Checking:${self.balance}")
        print(f"Savings:${self.balance2}")
        return self



    def yield_interest(self):
        self.balance = self.balance + self.balance*self.int_rate
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=.02, balance=0, balance2 = 0)
    def user_balance(self):
        self.account.display_account_info()

    def make_deposit(self, amount, account):
        self.account.deposit(amount,account)
        return self
    
    def make_withdrawl(self, amount, account):
        self.account.withdrawl(amount, account)
        return self
    def transfer(self, amount, other_user):
        self.account.withdrawl(amount, "Checking")
        other_user.account.deposit(amount, "Checking")
        return self

user1 = User("Jimmy", "Jimmy@gmail")
user2 = User("Tommy", "Tommy@gmail")

user1.make_deposit( 100, "Savings" ).make_deposit( 500, "Checking" ).make_withdrawl( 200, "Checking" ).make_withdrawl( 50, "Savings" ).transfer( 1, user2 ).user_balance()
user2.user_balance()


# my_bankAccount = BankAccount(.1, 100)
# my_bankAccount2 = BankAccount(.1,200)

# my_bankAccount.deposit(50).deposit(50).deposit(50).withdraw(50).display_account_info().yield_interest().display_account_info()
# my_bankAccount2.deposit(100).deposit(5000).withdraw(100).withdraw(200).withdraw(100).yield_interest().display_account_info()
