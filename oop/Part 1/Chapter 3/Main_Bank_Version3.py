# Test program using accounts
# Version 3, using a dictionary of account

# Bring in all the code from the Account class file 
from  Account import *

accountsDict = {}
nextAccountNumber = 0

# Create two accounts
account = Account('Joe', 100, 'joepassword')
joesAccountNumber = nextAccountNumber
accountsDict[joesAccountNumber] = account
print('Account number for Joe is: ', joesAccountNumber)
nextAccountNumber += 1

account = Account('Mary', 12345, 'MarysPassword')
marysAccountNumber = nextAccountNumber

accountsDict[marysAccountNumber] = account
print('Account number for Mary is: ', marysAccountNumber)
nextAccountNumber += 1

accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()
print()

# Call some methods on the different accounts...
print('Calling methods of the two accounts ...')
accountsDict[joesAccountNumber].deposit(50, 'joepassword')
accountsDict[marysAccountNumber].withdraw(345, 'MarysPassword')
accountsDict[marysAccountNumber].deposit(100, 'MarysPassword')

# Show the accounts
accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()

# Create another account with information from the user
print()
userName = input('What is the name for the new user account?: ')
userBalance = input('What is the starting balance for this account?: ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account?: ')
account = Account(userName, userBalance, userPassword)
newAccountNumber = nextAccountNumber
accountsDict[newAccountNumber] = account
print('Account Number for new account is: ', newAccountNumber)
nextAccountNumber += 1

# Show the newly created user account
accountsDict[newAccountNumber].show()

# Let's deposit 100 into the new account
accountsDict[newAccountNumber].deposit(100, userPassword)
usersBalance = accountsDict[newAccountNumber].getBalance(userPassword)
print()
print('After depositing 100, the user\'s balance is: ', usersBalance )

# Show the new Account
accountsDict[newAccountNumber].show()