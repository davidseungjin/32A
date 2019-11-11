def sum_numbers(numlist: [int]) -> int:
	'''Adds up the integers in a list of intergers'''
	total = 0

	for num in numlist:
		total += num

	return total

def sum_numbers2(numlist: [[int]]) -> int:
	'''Adds up the intergers in a list of lists of integers'''
	total = 0

	for sublist in numlist:
		for num in sublist:
			total += num

	return total

def sum_numbers3(numlist: [int or [int]]) -> int:
	'''
	Adds up the integers in a list whose elements are either integers or
	lists of integers
	'''
	total = 0

	for element in numlist:
		if type(element) == list:
			for num in element:
				total += num
		else:
			total += element

	return total



if __name__ == '__main__':
	print(sum_numbers([1,2,3,4,5]))
	print(sum_numbers([5, 8, 9, 3]))
	print(sum_numbers([4]))
	print(sum_numbers([]))

	print(sum_numbers2([[1,2],[3,4],[5,6,7]]))
	print(sum_numbers2([[1],[2],[3,4,5]]))
	print(sum_numbers2([[9]]))
	print(sum_numbers2([[]]))

	print(sum_numbers3([[1, 2, 3], 4, [5, 6], 7, 8]))
	print(sum_numbers3([1, 2, 3]))
	print(sum_numbers3([[1, 2], [3, 4], [5, 6]]))


