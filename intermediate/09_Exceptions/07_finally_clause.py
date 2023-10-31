# The finally clause

inventory = {
    'Piano': 3,
    'Lute': 1,
    'Sitar': 2
}

try:
    for name in inventory:
        print(name)
except KeyError:
    print('KeyError you have to write the correct name!')
else:
    print('Else This only execute if the program is working!')
# Write your code below:
finally:
    print('Always executed!')
