'''
4. Even Numbers
Create a list of numbers, print each number in the list that is even.
'''
number_list = [21, 44, 66, 77, 14, 20, 0]
even_list = []
for number in number_list:
    if number % 2 == 0:
        even_list.append(number)
print(even_list)