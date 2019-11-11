# sum_numbers1.py
#
# ICS 32A Fall 2019
# Code Example
#
# This function sums the numbers in a flat list of integers.  By "flat list",
# I mean that the list no sublists (i.e., every element is an integer).

def sum_numbers(numlist: [int]) -> int:
    '''Adds up the integers in a list of integers'''

    total = 0

    for num in numlist:
        total += num

    return total

print(sum_numbers([1,2,3,4,5]))
