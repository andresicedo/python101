'''
Fibonacci Sequence
Write a program that asks the user for a numerical input 'n'
It will then print out the corresponding fibonacci sequence values 
from 0 to 'n'
Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
This link is to help better understand what the fibonacci sequence
Essentially, (excluding the first two numbers of the sequence) you 
can get the next number of the sequence, by adding the last two 
numbers together
Example:
fib(4)
# n => fibSequence(n)
# 0 => 0
# 1 => 1
# 2 => 1
# 3 => 2
# 4 => 3
NOTE: It doesn't have to look exactly like this output, this was 
just for clarities sake
The next number is found by adding up the two numbers before it
'''
final = int(input("Enter the range number: "))
def fibonacci(final):
    first = 0
    second = 1
    third = 1
    sequence = [first, second, third]
    for number in sequence:
        number = sequence[-1] + sequence[-2]
        sequence.append(number)
        if final == len(sequence):
            break
    return sequence
output = fibonacci(final)
print(output)
        
