'''
2. Word Summary
Write a word_histogram program that asks the user for a sentence 
as its input, and prints a dictionary containing the tally of how 
many times each word in the alphabet was used in the text. 
For example:

$ python3 word_histogram.py
Please enter a sentence: To be or not to be
{'to': 2, 'be': 2, 'or': 1, 'not': 1}
'''
user_input = input("Please enter a sentence: ")
split = user_input.split(' ')
def word_histogram(split):
    word_count = {}
    for word in split:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count

output = word_histogram(split)
print(output)
