import socket

'''
This is the module for socket handling.
it contains 5 functions.
1. Make_connection: it is for making a connection to project2 server.
2. setup_io_between_server_client: it is to setup input/output with makefile.
3. output_stream_and_flush: to receive input from keyboard and stream it out to server.
4. input_stream: receiving server-input with readline function.
5. all_socket_close()
'''

def make_connection(mysocket: socket) -> None:
	'''
	This is an information of connection. 
	After made, socket connect to the address.
	'''
	connect_address = ('circinus-32.ics.uci.edu', 4444)
	mysocket.connect(connect_address)
	
def setup_io_between_server_client(mysocket: socket) -> None:
	'''
	This is to setup 'read' and 'write'
	'''
	input_stream = mysocket.makefile('r')
	output_stream = mysocket.makefile('w')
	return input_stream, output_stream

def output_stream_and_flush(mystring: str, output_stream) -> None:
	'''
	This is write function via network.
	It also include flush().
	'''
	output_stream.write(mystring + '\r\n')
	output_stream.flush()

def input_stream(input_stream) -> None:
	'''
	This is to read from the server connected.
	'''
	input_response = input_stream.readline()[:-1]
	return input_response

def all_socket_close(mysocket, input_stream, output_stream) -> None:
	'''
	This is to close all socket.
	'''
	input_stream.close()
	output_stream.close()
	mysocket.close()