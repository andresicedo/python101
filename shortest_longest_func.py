'''
1. Find the smallest number
Write a function smallest that accepts a List of numbers as an argument.

It should return the smallest number in the List.

#2. Find the largest number
Write a function largest that accepts a List of numbers as an argument.

It should return the largest number in the List.

'''
def smallest(list):
    small_Num = list[0]
    for number in list:
        if small_Num > number:
            small_Num = number
    return small_Num

output = smallest([2100, 35, 4, 3, 2, 1])
print(output)

def largest(list):
    largest_Num = list[0]
    for number in list:
        if largest_Num < number:
            largest_Num = number
    return largest_Num

output = largest([45, 54, 3600, 21, 3])
print(output)