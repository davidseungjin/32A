num = int(input())

for x in range(num):
    print('+-+', sep='')
    print('  '*x, '| |', sep='')
    print('  '*x, '+-', sep='', end='')

print('+')

