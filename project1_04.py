from pathlib import Path
from os.path import getsize

def print_d(mypath: Path) -> list:
	print('this is print_d function starting')
	temp = []
	for x in mypath.iterdir():
		if x.is_file():
			temp.append(x)
	b = sorted(temp)
	print('here below is print(x) in print_d')
	for x in b:
		print(x)
	'return-statement is necessary?'
	return b

def print_r(mypath: Path) -> list:
	a.extend(print_d(mypath))
	print('print_d funtion worked')
	for x in sorted(mypath.iterdir()):
		if x.is_dir():
			print('this is RECURSIVE')
			print_r(x)
	print('here below is print(x) in print_r')
	for x in a:
		print(x)
	return a

def print_a(b):
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
#	the_file = open(str(filepath), 'r')

#	print('print test for converting x from Path object to string object')
#	print(filepath)
#	print(str(filepath))

#	print('opening file test with using full path')
#	the_file = open('/users/davidlee/documents/github/32a/project1_01.py', 'r')

#	print('opening file test with using Path object')
	the_file = open(filepath, 'r')
#	test = the_file.readline()
#	print(test)

	while True:
		line = the_file.readline()
		if line.endswith('\n'):
			line = line[:-1]
			if mystring in line:
				print('this is the case we found the string')
				the_file.close()
				return True
		elif line == '':
			print('this is the case we ended with the empty string')
			the_file.close()
			return False
		else:
			print('this is the case we did not find nor ended with empty string')
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


def main_menu():
	myloop = True
	while myloop:
		myinput = input('Enter your input. for test, "D /Users" match it  ')
		mypath = Path(myinput[2:])
		if ((myinput.startswith('D') or myinput.startswith('R')) and(len(myinput)>2) and (myinput[1] == ' ') and (mypath.exists())):
			print("Match the rule")
			myloop = False
			if myinput[0] == 'D':
				print('your input is D')
				return print_d(mypath)
			elif myinput[0] == 'R':
				print('your input is R')
				return print_r(mypath)
		else:
			print("ERROR")
	print("out of while loop, thanks.")
	
def second_menu(b):
	myloop = True
	while myloop:
		myinput = input('Enter your second input. Q ANET<> and space+, that is enough at this time ')
		mystring = myinput[2:]
		if myinput == 'A':
			myloop = False
			print('input A')
			print_a(b)
		elif ((myinput.startswith('N') or myinput.startswith('E') or myinput.startswith('T') or myinput.startswith('<') or myinput.startswith('>')) and(len(myinput)>2) and (myinput[1] == ' ')):
			print("Match the rule")
			myloop = False
			if myinput[0] == 'N':
				print('input N')
				print_n(mystring)
			elif myinput[0] == 'E':
				print('input E')
				print_e(mystring)
			elif myinput[0] == 'T':
				print('input T')
				print_t(mystring)
			elif myinput[0] == '<':
				print('input <')
				print_lt(int(mystring))
			elif myinput[0] == '>':
				print('input >')
				print_gt(int(mystring))
		else:
			print("ERROR")
	print("out of while loop, thanks.")
	

if __name__ == '__main__':
	a = []
	maininput = main_menu()
	second_menu(maininput)

#	print('print a: let me see')
#	print(a)
