'''
1. Letter Summary
Write a letter_histogram program that asks the user for input, 
and prints a dictionary containing the tally of how many times 
each letter in the alphabet was used in the word. 
For example:
$ python3 letter_histogram.py
Please enter a word: banana
{'a': 3, 'b': 1, 'n': 2}
'''
user_input = input("Please enter a word: ")
def letter_histogram(user_input):
    letter_count = {}
    for string in user_input:
        if string not in letter_count:
            letter_count[string] = 1
        else:
            letter_count[string] += 1
    return letter_count

output = letter_histogram(user_input)
print(output)

