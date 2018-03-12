class Customer(object):

    def __init__(self, name, balance=0.00):
        self.name = name
        self.balance = balance
        julius = Customer('Julius Nyule', 2000.00)
        print('julius')

    def set_balance(self, balance = 0.00):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
        
