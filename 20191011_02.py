name = ''

while name == '':
    name = input('Enter your name: ')

    if name == '':
        print('Please enter a name; you entered nothing')

print('Your name is ' + name)
