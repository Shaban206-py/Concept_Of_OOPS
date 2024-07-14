#Encapsulatio
'''
Wrapping The data and function in a single unit (object)
'''

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount        
        print("Rs.", amount, "was debited")
        print("Your Total Balance :", self.get_balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credit")    
        print("Your Total Balance:", self.get_balance)  

    def get_balance(self):    
        return self.balance
    
acc1 = Account(10000, 1234567)
acc1.debit(1000)
acc1.credit(5000)
acc1.credit(500000)    
acc1.debit(10000)