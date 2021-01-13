'''
5. Positive Numbers
Create a list of numbers, print each number in the list that is 
greater than zero.
#6. Positive Numbers II
Create a list of numbers, create a new list which contains every 
number in the given list which is positive.
'''
number_list = [-1, 3, 5, -7, 21, -20, -14, 42, 12, -13, 0, 17, 1022]
positive = []
for number in number_list:
    if number > 0:
        positive.append(number)
print(positive)






