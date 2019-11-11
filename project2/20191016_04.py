def nested_sum(nested_list : 'nested list of integers') -> int:
	'''Adds up the integers in a nested list of integers'''

	total = 0

	for element in nested_list:
		if type(element) == list:
			total += nested_sum(element)
		else:
			total += element

	return total

if __name__ == '__main__':
	print(nested_sum([3, 6, 4]))
	print(nested_sum([[[1, 2], 3], 4]))
	print(nested_sum([[2, 7], [3, 8], [4, 9]]))
	print(nested_sum([1, [2, [3, [4, [5], 6], 7], 8], 9]))
	print(nested_sum([]))
