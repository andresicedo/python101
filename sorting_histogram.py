'''
3. Sorting a histogram
Given a histogram tally 
(one returned from either letter_histogram or word_histogram), 
print the top 3 words or letters.

$ python3 word_histogram_tally.py

Please enter a sentence: To be or not to be do be do be do
The top three words are:
be: 4
do: 3
to: 2
'''
tally = {'to': 2, 'be': 4, 'or': 1, 'not': 1, 'do': 3}
sorted_values = sorted(tally.values()) 
sorted_dict = {}


for i in sorted_values:# 1,1,2,3,4
    for k in tally.keys():#'to', 'be', 'or', 'not', 'do'
        if tally[k] == i:
            sorted_dict[k] = tally[k]
            break
#sorted_dict = {'or': 1, 'to': 2, 'do': 3, 'be': 4}

print(sorted_dict.items())

