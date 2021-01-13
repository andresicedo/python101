'''
7. Multiply a list
Create a list of numbers, and a single factor (also a number), 
create a new list consisting of each of the numbers in the first 
list multiplied by the factor. Print this list.
'''
number_list = [2, 4, 6, 8, 10]
factor = 3
new_list = []
for number in number_list:
    new_list.append(factor * number)
print(new_list)