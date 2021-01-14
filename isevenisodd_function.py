'''
4. is_even function
Write a function that accepts a number as an argument and 
returns a Boolean value. Return True if the number is even; 
return False if it is not even.
'''
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
output = is_even(31)
print(output)
'''
5. is_odd function
Write an is_odd function that uses your is_even function to determine 
if a number is odd. (That is, do not do the calculation - call a 
function that does the calculation.)

Hint: You'll use the not keyword.
'''
def is_odd(num):
    return not is_even(num)

output = is_odd(31)
print(output)