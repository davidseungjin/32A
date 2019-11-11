import connectfour

# This module has only two functions that provide a board and player on the board.


def board_copy(board: [[int]]):
	'''
	This have GameState board as an argument.
	and it shows column name at the first row
	then it shows COLUMN * ROW
	'''
	board_copy = board
	for x in range(connectfour.BOARD_COLUMNS):
		print('%d' % (x+1), end='\t')
	for y in range(connectfour.BOARD_ROWS):
		print()
		for x in range(connectfour.BOARD_COLUMNS):
			if board_copy[x][y] == 0:
				print('%s'%'.', end='\t')
			elif board_copy[x][y] == 1:
				print('%s'%'R', end='\t')
			elif board_copy[x][y] == 2:
				print('%s'%'Y', end='\t')
	print('\n')


def gaming_board(mystring, david):
	'''
	This has three function.
	The first is to update david object by applying column with
	functhings (e.g. drop, pop)

	The second is to check it has error by using try/exception.
	When DROP on the full column or POP the empty column, it raises
	error and simply printing 'DROP/POP ERROR' and require it once again
	'''

	myinput_command = mystring[:-2].lower()
	myinput_column = int(mystring[-1])-1

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
	board_copy(david.board)
	return david