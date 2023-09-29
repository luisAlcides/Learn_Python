from Account import *




if __name__=='__main__':
    account = Account('Homer', 100, 'password')
    account.show()

    newBalance = account.deposit(500, 'password')
    account.withdraw(250, 'password')
    currentBalance = account.getBalance('password')
    account.show()
    
    userName = input('What is the name for the new user account?: ')
    userBalance = int(input('What is the balance for the new user account?: '))
    userPassword = input('What is the password for the new user account?: ')
    
    newAccount = Account(userName, userBalance, userPassword)
    newAccount.show()
    
    newAccount.deposit(200, userPassword)
    userBalance = newAccount.getBalance(userPassword)
    print('After deposit of 200, the balance is', userBalance)
    