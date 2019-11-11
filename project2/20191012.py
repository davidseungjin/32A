from pathlib import Path


# p = Path('../Users/davidlee/documents/github/32a/test.txt')
p = Path('../Users/davidlee/documents/github/32a/')
print(p)
print(type(p))

q = p / Path('asdf.txt')

print(q)


r = p / 'asdfasdfasd.txt'
print(r)

print(p.is_file())
print(p.is_dir())

print(q.is_file())
print(q.is_dir())

print(r.is_file())
print(r.is_dir())



print(p.iterdir())

"""
the_file = open('test.txt', 'r')

while True:
    line = the_file.readline()

    if line == '':
        break
    elif line.endswith('\n'):
        line = line[:-1]

    print(line)

the_file.close()


the_file = open('test.txt', 'r')
line = the_file.readlines()
print(line)
the_file.close()

output_file = open('test_write.txt', 'w')
print(type(output_file))
print(output_file.mode)

output_file.write('Hello there\n')
output_file.write('David is ')
output_file.write('living everyday with the Lord')
output_file.close()

openthefile = open('test_write.txt', 'r')
while True:
    line = openthefile.readline()
    if line == '':
        break
    elif line.endswith('\n'):
        line = line[:-1]

    print(line)
"""

