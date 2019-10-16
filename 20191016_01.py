from pathlib import Path

p = Path('/Users/davidlee/documents/github/32A/')

print(p)
print(type(p))

q = p / Path('david01.txt')
print(q)

r = p / Path('david02.txt')
print(r)

print(p.exists())
print('================ p is file and p is dir =================')
print(p.is_file())
print(p.is_dir())
print('================ q is file and p is dir =================')
print(q.is_file())
print(q.is_dir())


f = q.open('w')
print(f)
#print(f.mode())
f.write('david01.txt\n')
f.write('word01\n')
f.write('word02\n')
f.write('word03\n')
f.write('word04\n')
f.write('word05\n')

f.close()

f = q.open('r')
print(f.readlines())
f.close()
print('================ directory iteration =====================')

print(p.iterdir())

print(list(p.iterdir()))
print()

for x in p.iterdir():
	print(x)


