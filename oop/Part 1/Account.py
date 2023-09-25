# Account class
class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password
        
    
    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        
        if amountToDeposit < 0:
            print('You cannot deposit a negative amount')
            return None
        
        self.balance = self.balance + amountToDeposit
        return self.balance
    
    
    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Incorrect password for this account')
            return None
        
        if amountToWithdraw < 0:
            print('You cannot withdraw a negative amount')
            return None
        
        if amountToWithdraw > self.balance:
            print('You cannot withdraw  more than you have in your account')
            return None
        
        self.balance = self.balance - amountToWithdraw
        return self.balance
    
    
    def getBalance(self, password):
        if password != self.password:
            print('Incorrect password for this account')
            return None
        
        return self.balance
    
    
    
    def show(self, password):
        if password != self.password:
            print('Incorrect password for this account')
            return None
        
        print('Account name: ' + self.name)
        print('Balance: ' + str(self.balance))
        print('Password: ' + self.password)
        print()
        return None
    
    
