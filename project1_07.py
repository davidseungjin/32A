from pathlib import Path
from os.path import getsize

def print_d(mypath: Path) -> list:
	temp = []
	for x in mypath.iterdir():
		if x.is_file():
			temp.append(x)
	b = sorted(temp)
#	for x in b:
#		print(x)
#	'return-statement is necessary?'
	return b

def print_r(mypath: Path) -> list:
	a.extend(print_d(mypath))
	for x in sorted(mypath.iterdir()):
		if x.is_dir():
#			print('print_r function called')
			print_r(x)
#	for x in a:
#		print('print x element in list a')
#		print(x)
	return a

def print_a(b: list) -> list:
	for x in b:
		print(x)
	return b

def print_n(mystring: str) -> list:
	mylist = []
	for x in a:
		if x.name == mystring:
			mylist.append(x)
	return mylist

def print_e(mystring: str) -> list:
	mylist = []
	if mystring[0] == '.':
		mystring2 = mystring[1:]
	else:
		mystring2 = mystring

	for x in a:
		if x.suffix[1:] == mystring2:
			mylist.append(x)
			print(x)
	return mylist

def textcheck(mystring: str, filepath: Path) -> bool:
	the_file = open(filepath, 'r')
	while True:
		line = the_file.readline()
		if line.endswith('\n'):
			line = line[:-1]
			if mystring in line:
				the_file.close()
				return True
		elif line == '':
			the_file.close()
			return False
		else:
			the_file.close()
			return False

def print_t(mystring: str) -> list:
	mylist = []
	for x in a:
		if textcheck(mystring, x):
			mylist.append(x)
			print(x)
	return mylist

def print_gt(myint: int) -> list:
	mylist = []
	for x in a:
		if getsize(x) > myint:
			mylist.append(x)
			print(x)
	return mylist

def print_lt(myint: int) -> list:
	mylist = []
	for x in a:
		if getsize(x) < myint:
			mylist.append(x)
			print(x)
	return mylist

def f_check(mylist: list) -> None:
	for x in mylist:
#		print('============')
#		print('before opening file')
		the_file = open(x, 'r')
#		print('before assigning readline of file')
		line = the_file.readline()
		line = line[:-1]
#		print('before printing file')
#		print(line)
#		print('before closing file')
		the_file.close()

def main_menu() -> list:
	myloop = True
	while myloop:
		myinput = input('')
		mypath = Path(myinput[2:])
		if ((myinput.startswith('D') or myinput.startswith('R')) and(len(myinput)>2) and (myinput[1] == ' ') and (mypath.exists())):
			myloop = False
			if myinput[0] == 'D':
				d = print_d(mypath)
				print_a(d)
				return d
			elif myinput[0] == 'R':
				r = print_r(mypath)
				print_a(r)
				return r
		else:
			print("ERROR")
#	print("out of while loop, thanks.")
	
def second_menu(b: list) -> list:
	myloop = True
	while myloop:
		myinput = input('')
		mystring = myinput[2:]
		if myinput == 'A':
			myloop = False
			print_a(b)
		elif ((myinput.startswith('N') or myinput.startswith('E') or myinput.startswith('T') or myinput.startswith('<') or myinput.startswith('>')) and(len(myinput)>2) and (myinput[1] == ' ')):
			myloop = False
			if myinput[0] == 'N':
				n = print_n(mystring)
				print_a(n)
				return n
			elif myinput[0] == 'E':
				e = print_e(mystring)
				print_a(e)
				return e
			elif myinput[0] == 'T':
				t = print_t(mystring)
				print_a(t)
				return t
			elif myinput[0] == '<':
				lt = print_lt(int(mystring))
				print_a(lt)
				return lt
			elif myinput[0] == '>':
				gt = print_gt(int(mystring))
				print_a(gt)
				return gt
		else:
			print("ERROR")
			'This is possible?'
#			return None David: you should not use this because it will effect of exiting loop

def third_menu(b: list) -> None:
	myloop = True
	while myloop:
		myinput = input('')
		if ((myinput == 'F') or (myinput == 'D') or (myinput == 'T')):
			myloop = False
			if myinput == 'F':
#				print('input F')
				f_check(b)
			elif myinput == 'D':
				print('input D')
			elif myinput == 'T':
				print('input T')
		else:
			print("ERROR")

		

if __name__ == '__main__':
	a = []
	myfirstmenu = main_menu()
	mysecondmenu = second_menu(myfirstmenu)

	third_menu(mysecondmenu)

	
