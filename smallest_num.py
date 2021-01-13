'''
3. Smallest Number
Create a list of numbers, print the smallest of the numbers.
'''
number_list = [21, 33, 54, 45, 1234]
smallest = number_list[4]
for number in number_list:
    if smallest > number:
        smallest = number

print(smallest)