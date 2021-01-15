'''
Fizz Buzz
Take a user's input for a number, and then print out all of the 
numbers from 1 to that number.
For any number divisible by 3, print 'fizz'
For any number divisible by 5, print 'buzz'
For any number divisible by 3 and 5, print 'fizzbuzz'
Example:

fizzbuzz(15)
#1
#2
#fizz
#4
#buzz
#6
#7
#8
#fizz
#buzz
#11
#fizz
#13
#14
#fizzbuzz
'''
print("We will begin the game at 1")
user_input = int(input("Please enter the final number: "))
def fizzbuzz(user_input):
    begin = 1
    while begin < user_input:
        if begin % 3 == 0 and begin % 5 == 0:
            print("#fizzbuzz")
            break
        if begin % 3 == 0:
            print("#fizz")
        elif begin % 5 == 0:
            print("#buzz")
        else:
            print(f"#{begin}")
        begin = begin + 1
    return begin
output = fizzbuzz(user_input)
print(output)