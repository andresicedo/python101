'''
2. Largest Number
Create a list of numbers, print the largest of the numbers.
'''
number_list = [21, 33, 54, 45, 1234]
largest = number_list[0]
for number in number_list:
    if largest < number:
        largest = number

print(largest)