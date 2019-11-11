import collections

NONE = 0
RED = 1
YELLOW = 2

BOARD_COLUMNS = 3
BOARD_ROWS = 2

GameState = collections.namedtuple('GameState', ['board', 'turn'])

class InvalidMoveError(Exception):
	'''Raised whenever an invalid move is made'''
	pass

class GameOverError(Exception):
	'''Raised whenever an attempt is made to make a move after the game is already over'''
	pass

def new_game() -> GameState:
	return GameState(board = _new_game_board(), turn = Red)

def _new_game_board() -> [[int]]:
	board = []
	for col in range(BOARD_COLUMNS):
		board.append([])
		print('column loop')
		for row in range(BOARD_ROWS):
			print('row %d loop'%row)
			# print('board itself before append', board)
			# print('board[0] before append', board[0])
			# print('board[-1] before append', board[-1])
			board[-1].append(row)
			# print('board itself after append', board)
			# print('board[0] after append', board[0])
			# print('board[-1] after append', board[-1])
			

	return board


if __name__ == '__main__':
	board = _new_game_board()

	print(board)