# Bank 2

accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password
    

def show():
    global accountPassword, accountBalance, accountName
    print('Name: ', accountName)
    print('Balance: ', accountBalance)
    
    
def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Incorrect password')
        return None
    return accountBalance


def deposit(amount, password):
    global accountName, accountBalance, accountPassword
    if amount < 0:
        print('You cannot deposit a negative amount!')
        return None
    
    if password != accountPassword:
        print('Incorrect password')
        return None
    
    accountBalance = accountBalance + amount
    return accountBalance


def withdraw(amount, password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Incorrect password')
        return None
    
    if amount < 0:
        print('You cannot withdraw a negative amount')
        return None
    
    if amount > accountBalance:
        print('You cannot withdraw more than you have in your account')
        return None
    
    
    accountBalance -= amount
    return accountBalance
    
    

newAccount('Bob', 100, 'soup')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()
    
    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0] # just use first letter
    print()
    
    if action == 'b':
        print('Get Balance: ')
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print('Balance: ', theBalance)
    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter the amount to deposit: ')
        userDepositAmount = float(userDepositAmount)
        userPassword = input('Please enter the password: ')
        
        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print('New Balance: ', newBalance)
    elif action == 's':
        print('Show Account: ')
        show()
    elif action == 'w':
        print('Withdraw: ')
        userWithdrawAmount = input('Please enter the amount to withdaw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')
        
        newBalance = withdraw(userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('New Balance: ', newBalance)
    elif action == 'q':
        break
    else:
        print('Unknown command: ', action)
        
print('Goodbye!')
    