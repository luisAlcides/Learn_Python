# The else clause execute only if the progam work

# Checkpoint 1
customer_rewards = {
    'Zoltan': 82570,
    'Guadalupe': 29850,
    'Mario': 17849
}


def display_rewards_account(customer):
    # Checkpoint 2
    try:
        rewards_number = customer_rewards[customer]
    except KeyError:
        print('Customer was not found in rewards program!')
    # Checkpoint 3
    else:
        print('Rewards account number is: ' + str(rewards_number))


# Checkpoint 4
customer = 'Mario'
display_rewards_account(customer)
