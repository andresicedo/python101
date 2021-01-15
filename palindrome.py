'''
Palindrome Check
What is a palindrome? A word that is spelled the same backward and forward.
Example: "racecar", "hannah", "tot"
Write a function that takes in a string and returns a boolean (true/false) 
representing whether the string is a palindrome or not.
Example:

# 'racecar' => true
# 'banana' => false
# 'dud' => true
# 'pancakes' => false


- NOTE: It doesn't have to look exactly like this output, this was just 
for clarities sake
'''
string = input("Please enter an expression: ")
def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
output = palindrome(string)
print(output)
