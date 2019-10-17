from pathlib import Path



def print_d(mypath):
	a = []
	for x in mypath.iterdir():
		if x.is_file():
			a.append(x)
	b = sorted(a)
	for x in b:
		print(x)
	'return-statement is necessary?'
	return b

def print_r(mypath):
	a = print_d(mypath)
	for x in mypath.iterdir():
		if x.is_dir():
			a.append(x)
	b = sorted(a)
	for x in b:
		if x.is_dir():
			print_r(x)
		else:
			print(f'This is {x} and it is maybe')
	

def main_menu():
	myloop = True
	while myloop:
		myinput = input('Enter your input. for test, "D /Users" match it  ')
		mypath = Path(myinput[2:])

		if ((myinput.startswith('D') or myinput.startswith('R')) and(len(myinput)>2) and (myinput[1] == ' ') and (mypath.exists())):
			print("Match the rule")
			myloop = False
			if myinput[0] == 'D':
				print_d(mypath)
			elif myinput[0] == 'R':
				print_r(mypath)
		else:
			print("ERROR")
	print("out of while loop, thanks.")
	
def second_menu():
	myloop = True
	while myloop:
		myinput = input('Enter your second input. Q ANET<> and space+, that is enough at this time ')
		mystring = myinput[2:]
		if ((myinput.startswith('A') or myinput.startswith('N') or myinput.startswith('E') or myinput.startswith('T') or myinput.startswith('<') or myinputstartswith('>')) and(len(myinput)>2) and (myinput[1] == ' ')):
			print("Match the rule")
			myloop = False
			if myinput[0] == 'A':
				print('input A')
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
	main_menu()
	second_menu()
