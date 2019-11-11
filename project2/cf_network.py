import connectfour
import i32cfsp_sockethandling
import boardshow
import cf_console
import socket

def greeting_words(input_stream, output_stream):
	'''
	it is to login.
	If client provide UCInetID, then it cancatenate string 'I32CFSP_HELLO'
	with the input to make complete string.
	'''
	mystring = input('Please UCInetID: ')
	i32cfsp_sockethandling.output_stream_and_flush('I32CFSP_HELLO '+ mystring, output_stream)
	i32cfsp_sockethandling.input_stream(input_stream)
	
def passcode_for_game_start(input_stream, output_stream):
	'''
	This is to get input passcode 'AI_GAME'
	it will loop until user input exactly matches to 'AI_GAME'
	'''
	mystring = input('input what do you want? ')
	while mystring != 'AI_GAME':
		mystring = input('type error. input again. input what do you want? ')
	i32cfsp_sockethandling.output_stream_and_flush(mystring, output_stream)
	i32cfsp_sockethandling.input_stream(input_stream)

def client_input(input_stream, output_stream, david):
	'''
	This is to get client input.
	Error handling is also included
	'''
	mystring = input('what do you want to input? ')
	while not (mystring.startswith('DROP') or mystring.startswith('POP')):
		mystring = input('type error. what do you want to input? ')
	i32cfsp_sockethandling.output_stream_and_flush(mystring, output_stream)
	return mystring, david

def server_response(input_stream, output_stream, david):
	'''
	This is to read server_response.
	'''
	mystring = i32cfsp_sockethandling.input_stream(input_stream)
	print(mystring)
	while mystring not in ('READY'):
		mystring = i32cfsp_sockethandling.input_stream(input_stream)
		print(mystring)
		if (mystring.startswith('DROP') or mystring.startswith('POP')):
			mystring2 = mystring
		if (mystring.startswith('WINNER_')):
			mystring2 = mystring
	return mystring2, david
		

def game_playing_until_winner(input_stream, output_stream, david):
	'''
	This is main playing function. It calls three function. 
	Two are in this module and the other one is coming from external module
	The first two are 'client input' and 'server input'.
	The other one is the function to show board.
	The game will continue until server says 'WINNER~'
	'''
	mystring, david = client_input(input_stream, output_stream, david)
	david = boardshow.gaming_board(mystring, david)
	mystring, david = server_response(input_stream, output_stream, david)
	david = boardshow.gaming_board(mystring, david)
	while mystring not in ('WINNER_RED', 'WINNER_YELLOW'):
		try:
			mystring, david = client_input(input_stream, output_stream, david)
			if mystring.startswith('WINNER_'):
				return
			david = boardshow.gaming_board(mystring, david)
			if mystring.startswith('WINNER_'):
				return
			mystring, david = server_response(input_stream, output_stream, david)
			if mystring.startswith('WINNER_'):
				return
			david = boardshow.gaming_board(mystring, david)
			if mystring.startswith('WINNER_'):
				return
		except:
			print('Input error')
		
def game_close(mysocket, input_stream, output_stream):
	'''
	Game close is for closing sockets.
	'''
	i32cfsp_sockethandling.all_socket_close(mysocket, input_stream, output_stream)


if __name__ == '__main__':
	'''
	Main function consists several ones.
	Creating game --> Making connection --> Define input_stream and output stream
	After that, Introductory words --> game play --> game close will go on.
	'''
	david = connectfour.new_game()			# creating game
	mysocket = socket.socket()					# creating socket
	
	i32cfsp_sockethandling.make_connection(mysocket)			# socket connection to the address
	input_stream, output_stream = i32cfsp_sockethandling.setup_io_between_server_client(mysocket)							# setup input/output

	greeting_words(input_stream, output_stream)						# client input of ID
	passcode_for_game_start(input_stream, output_stream)	# client input of 'AI_GAME'
	game_playing_until_winner(input_stream, output_stream, david)
	game_close(mysocket, input_stream, output_stream)			# closing socket
	