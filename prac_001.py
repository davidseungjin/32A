first = 10
last = 30
last - first
print(last-first)

text = '     David      '

print(text)
print(text.strip())
print(text.upper())
print(text.isupper())

num = int(input('Enter a number: '))

while num > 0:
    print(num)
    num -= 1

print('Goodbye!')

while True:
    name = input('Enter your name: ')

    if name == '':
        print('Please enter your name; you enteres nothing')
    else:
        break
print('Your name is ' + name)
