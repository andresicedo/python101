'''
6. only_evens function
Write a function that accepts a List of numbers as an argument.

Return a new List that includes the only the even numbers.

only_evens([11, 20, 42, 97, 23, 10])
# Returns [20, 42, 10]
Hint: use your is_even() function to determine which numbers to 
include in your new List.
'''
def only_evens(list):
    evens = []
    for even_Num in list:
        if even_Num % 2 == 0:
            evens.append(even_Num)
    return evens

output = only_evens([2, 4, 21, 8, 36, 37])
print(output)
'''
#7. only_odds function
Write a function that accepts a List of numbers as an argument.

Return a new List that includes the only the odd numbers.

only_odds([11, 20, 42, 97, 23, 10])
# Returns [11, 97, 23]
Hint: use your is_odd() function to determine which numbers 
to include in your new List.
'''
def only_odds(list):
    odds = []
    for odd_Num in list:
        if odd_Num % 2 == 1:
            odds.append(odd_Num)
    return odds

output = only_odds([3, 4, 21, 9, 36, 37])
print(output)