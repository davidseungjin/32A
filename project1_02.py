from pathlib import Path



def my_d(mypath: Path) -> list:
	for x in mypath.iterdir():
		if x.is_file():
			a.append(x)
	b = sorted(a)
	return b

def my_r(mypath: Path) -> list:
	my_d(mypath)
	for x in mypath.iterdir():
		if x.is_dir():
			my_r(mypath)
	b = sorted(a)
	return b

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
				mylist = my_d(mypath)
				for x in mylist:
					print(x)
				return mylist
			elif myinput[0] == 'R':
				return my_r(mypath)
		else:
			print("ERROR")
	print("out of while loop, thanks.")
	
def second_menu(b):
	myloop = True
	while myloop:
		myinput = input('Enter your second input. Q ANET<> and space+, that is enough at this time ')
		mystring = myinput[2:]
		if ((myinput.startswith('A') or myinput.startswith('N') or myinput.startswith('E') or myinput.startswith('T') or myinput.startswith('<') or myinputstartswith('>')) and(len(myinput)>2) and (myinput[1] == ' ')):
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
#	second_menu(maininput)
