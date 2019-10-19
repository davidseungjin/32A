from pathlib import Path



def print_d(mypath: Path) -> list:
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
#	b = sorted(a)
	print('here below is print(x) in print_r')
	for x in a:
		print(x)
	return a

def print_a(b):
	for x in b:
		print(x)
	return b

def main_menu():
	myloop = True
	while myloop:
		myinput = input('Enter your input. for test, "D /Users" match it  ')
		mypath = Path(myinput[2:])

		if ((myinput.startswith('D') or myinput.startswith('R')) and(len(myinput)>2) and (myinput[1] == ' ') and (mypath.exists())):
			print("Match the rule")
			myloop = False
			if myinput[0] == 'D':
				return print_d(mypath)
			elif myinput[0] == 'R':
				return print_r(mypath)
		else:
			print("ERROR")
	print("out of while loop, thanks.")
	
def second_menu(b):
	myloop = True
	while myloop:
		myinput = input('Enter your second input. Q ANET<> and space+, that is enough at this time ')
		mystring = myinput[2:]
		if ((myinput.startswith('A') or myinput.startswith('N') or myinput.startswith('E') or myinput.startswith('T') or myinput.startswith('<') or myinput.startswith('>')) and(len(myinput)>2) and (myinput[1] == ' ')):
			print("Match the rule")
			myloop = False
			if myinput[0] == 'A':
				print('input A')
				print_a(b)
			elif myinput[0] == 'N':
				print('input N')
			elif myinput[0] == 'E':
				print('input E')
			elif myinput[0] == 'T':
				print('input T')
			elif myinput[0] == '<':
				print('input <')
			elif myinput[0] == '>':
				print('input >')
		else:
			print("ERROR")
	print("out of while loop, thanks.")
	

if __name__ == '__main__':
	a = []
	maininput = main_menu()
	second_menu(maininput)
