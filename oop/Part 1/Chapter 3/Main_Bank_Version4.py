from Account import *

accountsDict = {}
nextAccountDict = 0

# snip creating accounts, adding them to dictionary

def inputUser(pressType, action):
    print(f'*** {pressType} ***')
    if action == 'o':
        userName = input('What is the name for the new user account? ')
        userStartingAmount = input('What is the starting balance for this account? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What is the password you want to use for this account? ')
        oAccount = Account(userName, userStartingAmount, userPassword)
        accountsDict[nextAccountNumber] = oAccount
        print('Your new account number is:', nextAccountNumber)
        nextAccountNumber = nextAccountNumber + 1
        print()
    else:
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Please enter the password: ')
        theBalance = 0
        if action == 'b':
            theBalance = account.getBalance(userAccountPassword)
        elif action == 'd':
            userDepositAmount = int(input('Please enter the account: '))
            theBalance = account.deposit(userDepositAmount,userAccountPassword)
        elif action == 'w':
            userWithdrawalAmount = input('Please enter the amount to withdraw: ')
            userWithdrawalAmount = int(userWithdrawalAmount)
            theBalance = account.withdraw(userWithdrawalAmount, userPassword)
            if theBalance is not None:
                print('Withdrew:', userWithdrawalAmount)
        elif action == 's':
            for userAccountNumber in accountsDict:
                account = accountsDict[userAccountNumber]
                print(' Account number:', userAccountNumber) 
                account.show()
        account = accountsDict[userAccountNumber]
        if theBalance is not None:
            print('Your balance is: ', theBalance)

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press o to open a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()
    
    action = input('What do you want to do?: ')
    action = action.lower()
    action = action[0]
    print()
    
    
    if action == 'b':
        inputUser('Get Balance', action)
    elif action == 'd':
        inputUser('Deposit', action)
    elif action == 'o':
        inputUser('Open new account', action)
    elif action == 'w':
        inputUser('Make Withdrawal', action)
    elif action == 's':
        inputUser('Account', action)  
    elif action == 'q':
        break  