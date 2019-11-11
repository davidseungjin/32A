def davidlee(num: int) -> int:
	return num**3

if __name__ == '__main__':
	for x in range(0, 20, 2):
		print(x)

	x = int(input('Enter your number. I will provide a calculated answer '))
	print(davidlee(x))
