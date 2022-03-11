def add(num1:int,num2:int):
    return num1+num2

class BankAccount():
    def __init__(self,intial_amount=0):
        self.balance=intial_amount
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if self.balance < amount:
            raise Exception("Insuffcient funds")
        self.balance -= amount
    def collect_interest(self):
        self.balance *= 1.1
