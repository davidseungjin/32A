import connectfour
import boardshow


def input_check(myinput: str) -> bool:
	'''
	Ths is to check input.
	Once it receive input. Error raises when error happens.
	White spaces are stripped.
	And, lower letter are compared to two words, 'drop' or 'pop'
	If column number is out of range, it raises False flag.
	'''
	try:
		myinput_command = myinput[:-2].lower().strip()
		myinput_column = int(myinput[-1])-1
		if ((myinput_command != 'drop') and (myinput_command != 'pop')):
			return False
		if (myinput_column > 6 or myinput_column < 0):
			return False
		return True
	except:
		return False

def cf_console_play(david: connectfour.GameState):
	'''
	This is main play function. Basically, it execute as long as 
	winner is not decided yet (means winner is zero)
	'''
	while connectfour.winner(david) == 0:
			myinput = input('\nplease select drop OR pop, and column. ex) drop 4 ')
			'''
			After getting input value, below function will execute input validation.
			'''
			while not input_check(myinput):
				myinput = input('\nType error. Select drop OR pop, and column. ex) drop 4 ')
			
			'''
			If the input passes input_check (input validation), input is parsed by two parts.
			The first part is the command (either drop or pop), and the second part
			is column.
			'''
			myinput_command = myinput[:-2].lower()
			myinput_column = int(myinput[-1])-1

			'''
			cases are two. drop and pop. 
			However, the one other thing to consider is error handling. when drop in
			a full column or pop an empty column, I should put error handling.
			'''
			if myinput_command == 'drop':
				try:
					david = connectfour.drop(david, myinput_column)
				except:
					print('DROP ERROR')
			elif myinput_command == 'pop':
				try:
					david = connectfour.pop(david, myinput_column)
				except:
					print('POP ERROR')

			'''
			After performm one turn, game shows board to see where are players on the board.
			'''
			boardshow.board_copy(david.board)
			print()
	return connectfour.winner(david)
	

def winner_convert(mywinner: int) -> str:
	'''
	It is just to convert integers that represent winner to
	NONE / RED / YELLOW
	'''
	if mywinner == 0:
		print('NONE')
	elif mywinner == 1:
		print('RED')
	elif mywinner == 2:
		print('YELLOW')


if __name__ == '__main__':
	'''
	main executable consists of three components.
	The first one is creating new game by calling the method.
	The second function is main function of playing console game.
	The third one is to printing winner once made.
	'''
	david = connectfour.new_game()
	david_result = cf_console_play(david)
	
	print()
	winner_convert(david_result)
	