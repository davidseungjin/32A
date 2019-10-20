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
			print('print_r function called')
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
			print(x)
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


def main_menu() -> list:
	myloop = True
	while myloop:
		myinput = input('Enter your input. for test, "D /Users" match it  ')
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
		myinput = input('Enter your second input. Q ANET<> and space+, that is enough at this time ')
		mystring = myinput[2:]
		if myinput == 'A':
			myloop = False
			print_a(b)
		elif ((myinput.startswith('N') or myinput.startswith('E') or myinput.startswith('T') or myinput.startswith('<') or myinput.startswith('>')) and(len(myinput)>2) and (myinput[1] == ' ')):
			myloop = False
			if myinput[0] == 'N':
				print_n(mystring)
			elif myinput[0] == 'E':
				print_e(mystring)
			elif myinput[0] == 'T':
				print_t(mystring)
			elif myinput[0] == '<':
				print_lt(int(mystring))
			elif myinput[0] == '>':
				print_gt(int(mystring))
		else:
			print("ERROR")
#	print("out of while loop, thanks.")
	

if __name__ == '__main__':
	a = []
	maininput = main_menu()
	second_menu(maininput)

