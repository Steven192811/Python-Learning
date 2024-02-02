# For this challenge, create a bank account class that has two attributes:
# owner
# balance

# and two methods:

# deposit
# withdraw

# As an added requirement, withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and test
# to make sure the account can't be overdrawn.

#Example

class Simple():
    def __init__(self,value):
        self.value = value

    def add_to_value(self,amount):
        self.value = self.value + amount
        print(f"We just added {amount} to your value")

# myobj = Simple(300)
# print(myobj.value)
# myobj.add_to_value(500) # We just added 500 to your value
# print(myobj.value) # 800


# Solution

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount # self.balance = self.balance + amount
        print(f"Deposited {amount} into {self.owner}'s account")

    def withdraw(self, amount):
        if amount >= self.balance: # If the amount is greater than the balance
            print(f"Insufficient funds! {self.owner}'s account balance is {self.balance}")
        else:
            self.balance -= amount # self.balance = self.balance - amount
            print(f"Withdrew {amount} from {self.owner}'s account")

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"

# 1. Instantiate the class
acct1 = Account('Steven',100)
print(acct1) # Account owner: Steven Account balance: 100

# 2. Print the object
print(acct1) # Account owner: Steven Account balance: 100

# 3. Show the account owner attribute
print(acct1.owner) # Steven

# 4. Show the account balance attribute
print(acct1.balance) # 100

# 5. Make a series of deposits and withdrawals
acct1.deposit(50) # Deposited 50 into Steven's account
print(acct1) # Account owner: Steven Account balance: 150

acct1.withdraw(75) # Withdrew 75 from Steven's account
print(acct1) # Account owner: Steven Account balance: 75

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500) # Insufficient funds! Steven's account balance is 75
print(acct1) # Account owner: Steven Account balance: 75
