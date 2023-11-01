# Assert statement

def times_ten(number):
    return number * 10


result = times_ten(20)
assert result == 200, 'Expected times_ten(20) to return 200, instead got ' + str(result)


# Practice
print()
print()

destinations = {
    'BUD': 'Budapest',
    'CMN': 'Casablanca',
    'IST': 'Istanbul'
}


print('Welcome to Small World Airlines!')
print('What is the airport code of your travel destination?')
destination = 'HND'

assert destination in destinations, 'Sorry, Small World currently does not fly to this destination!'
city_name = destinations[destination]
print('Great! Retrieving information for your flight to ... ' + city_name)
