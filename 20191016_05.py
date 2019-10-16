def user_interface() -> None:
	'''
	Repeatedly asks the user to specify a file; each time, the number of lines of text
	in the file are printed, unless the file could not be opened, in which case a
	brief error message is displayed instead
	'''

	while True:
		file_path = input('What file? ').strip()
		
		if file_path == '':
			break

		try:
			lines_in_file = count_lines_in_file(file_path)
			print('{} line(s) in {}'.format(lines_in_file, file_path))
		except OSError:
			print('Filed to open the file successfully')
		except ValueError:
			print('Failed to read from the file succesfully;l it is not a text file')


if __name__ == '__main__':
	user_interface()
