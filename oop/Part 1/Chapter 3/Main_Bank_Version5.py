from Bank import *

# Create an instance of the Bank
bank = Bank()

# Main code
# Create two test accounts
joesAccountNumber = bank.createAccount('Joe', 100, '1234')
print('Joe\'s account number is: ', joesAccountNumber)

marysAccountNumber = bank.createAccount('Mary', 200, '5678')
print('Mary\'s account number is: ', marysAccountNumber)

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press x')  # Changed the option for closing an account
    print('To make a deposit, press d')  # Changed the option for making a deposit
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        bank.balance()
    elif action == 'x':  # Changed the option for closing an account
        bank.closeAccount()
    elif action == 'd':  # Changed the option for making a deposit
        bank.deposit()
    elif action == 'o':
        bank.openAccount()
    elif action == 's':
        bank.show()
    elif action == 'q':
        break
    elif action == 'w':
        bank.withdraw()
    else:
        print('Unrecognized command: ', action)

print('Done')