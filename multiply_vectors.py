'''
1. Multiply Vectors
Given two lists of numbers of the same length, create a new list 
by multiplying the pairs of numbers in corresponding positions 
in the two lists. 

Example:

[2, 4, 5] x [2, 3, 6] = [4, 12, 30
'''
list_one = [2, 4, 6, 8]
list_two = [3, 6, 9, 12]
new_list = []
for num1, num2 in zip(list_one, list_two):
    new_list.append(num1 * num2)
print(new_list)