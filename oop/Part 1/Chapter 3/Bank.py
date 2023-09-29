from Account import *

class Bank:
    def __init__(self, hours, address, phone):
        self.accountsDict = {}
        self.nextAccountNumber = 0
        self.hours = hours
        self.address = address
        self.phone = phone


    def askForValidAccountNumber(self):
        accountNumber = input('What is your account Number? ')
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            raise AbortTransaction('The account number must be an integer')
        if accountNumber not in self.accountsDict:
            raise AbortTransaction('There is no account ' + str(accountNumber))
        return accountNumber
    
    def getUserAccount(self):
        accountNumber = self.askForValidAccountNumber()
        account = self.accountsDict[accountNumber]
        self.askForValidPassword(account)
        return account


    def createAccount(self, theName, theStartingAmount, thePassword):
        account = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.nextAccountNumber += 1
        self.accountsDict[newAccountNumber] = account  # Agregar la cuenta al diccionario
        return newAccountNumber


    def openAccount(self):
        print("Opening an account")
        userName = input('What is the name for the new user account? ')
        userStartingAmount = int(input('How much money is the user starting with? '))
        userPassword = input('What is the password for the new user account? ')

        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print('The new account number is: ', userAccountNumber)
        print()


    def closeAccount(self):
        print('Close Account')
        userAccountNumber = int(input('What is the account number? '))
        userPassword = input('What is the password? ')
        account = self.accountsDict.get(userAccountNumber)
        if account is not None:
            theBalance = account.getBalance(userPassword)
            if theBalance is not None:
                print('You had', theBalance, 'in your account, which is being returned to you.')
                # Remove user's account from the dictionary of accounts
                del self.accountsDict[userAccountNumber]
                print('Your account is now closed.')
        else:
            print('Account not found.')


    def balance(self):
        print('Get Balance')
        userAccountNumber = int(input('What is the account number? '))
        userAccountPassword = input('Please enter the password: ')
        account = self.accountsDict.get(userAccountNumber)
        if account is not None:
            theBalance = account.getBalance(userAccountPassword)
            if theBalance is not None:
                print('Your balance is: ', theBalance)
        else:
            print('Account not found.')


    def deposit(self):
        print('Deposit')
        account = self.getUserAccount()
        depositAmount = int(input('Please enter amount to deposit: '))
        theBalance = account.deposit(depositAmount)
        print('Deposited: ', depositAmount)
        print('Your new balance is: ', theBalance)


    def show(self):
        print('Show')
        print('(This would typically require an admin password)')
        for userAccountNumber in self.accountsDict:
            account = self.accountsDict[userAccountNumber]
            print('Account: ', userAccountNumber)
            account.show()
            print()


    def withdraw(self):
        print('*** Withdraw ***')
        account = self.getUserAccount()
        userAmount = int(input('Please enter the amount to withdraw:'))
        theBalance = account.withdraw(userAmount)
        print('Withdrawn: ', userAmount)
        print('Your new balance is: ', theBalance)
    
    
    def getInfo(self):
        print('Hours:', self.hours)
        print('Address:', self.address)
        print('Phone:', self.phone)
        print('We currently have ', len(self.accountsDict), 'accounts in our bank.')
        print()
        