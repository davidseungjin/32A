from pathlib import Path
from os.path import getsize
from shutil import copy


def print_d(mypath: Path) -> [Path]:
	'In the first menu between D and R, function for D'
	temp = []
	for x in mypath.iterdir():
		if x.is_file():
			temp.append(x)
	b = sorted(temp)
	return b

def print_r(mypath: Path) -> [Path]:
	'In the first menu between D and R, function for R'
	a.extend(print_d(mypath))
	for x in sorted(mypath.iterdir()):
		if x.is_dir():
			print_r(x)
	return a

def print_a(b: [Path]) -> [Path]:
	'It is printing function exist mainly because many menu requires printing result'
	for x in b:
		print(x)
	return b

def print_n(mystring: str) -> [Path]:
	'In the second menu among N, E, T, <, >, it is for N'
	mylist = []
	for x in a:
		if x.name == mystring:
			mylist.append(x)
	return mylist

def print_e(mystring: str) -> [Path]:
	'In the second menu among N, E, T, <, >, it is for E'
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
	'In the second menu among N, E, T, <, >, it is used for T.'
	'I left the function of checking text separate from making list when push T'
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

def print_t(mystring: str) -> [Path]:
	'In the second menu among N, E, T, <, >, it is for T.'
	mylist = []
	for x in a:
		if textcheck(mystring, x):
			mylist.append(x)
			print(x)
	return mylist

def print_gt(myint: int) -> [Path]:
	'In the second menu among N, E, T, <, >, it is for >.'
	mylist = []
	for x in a:
		if getsize(x) > myint:
			mylist.append(x)
			print(x)
	return mylist

def print_lt(myint: int) -> [Path]:
	'In the second menu among N, E, T, <, >, it is for <.'
	mylist = []
	for x in a:
		if getsize(x) < myint:
			mylist.append(x)
			print(x)
	return mylist

def f_check(mylist: [Path]) -> None:
	'In the third menu among F D T, it is for F.'
	for x in mylist:
		try:
			the_file = open(x, 'r')
			line = the_file.readline()
			line = line[:-1]
			print(line)
		except:
			print('NOT TEXT')
	the_file.close()

def d_check(mylist: [Path]) -> None:
	'In the third menu among F D T, it is for D.'
	for x in mylist:
		y = str(x) + ".dup"
		copy(x, y)

def t_check(mylist: [Path]) -> None:
	'In the third menu among F D T, it is for T.'
	for x in mylist:
		x.touch()

def main_menu() -> list:
	'It is the first menu'
	myloop = True
	while myloop:
		myinput = input('')
		mypath = Path(myinput[2:])
		if ((myinput.startswith('D') or myinput.startswith('R')) 
		and(len(myinput)>2) and (myinput[1] == ' ') and (mypath.exists())):
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
	
def second_menu(b: [Path]) -> [Path]:
	'It is the second menu'
	myloop = True
	while myloop:
		myinput = input('')
		mystring = myinput[2:]
		if myinput == 'A':
			myloop = False
			print_a(b)
		elif ((myinput.startswith('N') or myinput.startswith('E') or 
		myinput.startswith('T') or myinput.startswith('<') or 
		myinput.startswith('>')) and (len(myinput)>2) and (myinput[1] == ' ')):
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

def third_menu(b: Path) -> None:
	'It is the third menu'
	myloop = True
	while myloop:
		myinput = input('')
		if ((myinput == 'F') or (myinput == 'D') or (myinput == 'T')):
			myloop = False
			if myinput == 'F':
				f_check(b)
			elif myinput == 'D':
				d_check(b)
			elif myinput == 'T':
				t_check(b)
		else:
			print("ERROR")

if __name__ == '__main__':
	a = []
	myfirstmenu = main_menu()
	mysecondmenu = second_menu(myfirstmenu)

	third_menu(mysecondmenu)

