import socket

example_socket = socket.socket()
print(type(example_socket))

connecting_address = ('128.195.1.83', 5151)
example_socket.connect(connecting_address)

input_stream = example_socket.makefile('r')
output_stream = example_socket.makefile('w')

output_stream.write('DavidLee is trying to learn Python.\r\n')
output_stream.flush()

input_stream.readline()

input_stream.close()
output_stream.close()
socket.close()


