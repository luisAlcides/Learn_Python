# Main program for controlling a bank made up of accounts
from Bank import *

# create an instance of the bank
bank = Bank('9 to 5', '123 Main St', '555-555-5555')

# Main code

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To get bank information, press i')
    print('To open an account, press o')
    print('To quit, press q')
    print('To make a withdrawal, press w')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w')
    print()
    
    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()
    
    try:
        if action == 'b':
            bank.balance()
        elif action == 'c':
            bank.closeAccount()
        elif action == 'd':
            bank.deposit()
        elif action == 'i':
            bank.getInfo()
        elif action == 'o':
            bank.openAccount()
        elif action == 'q':
            break
        elif action == 's':
            bank.show()
        elif action == 'w':
            bank.withdraw()
    
    except AbortTransaction as error:
        print(error)
    
print('done')