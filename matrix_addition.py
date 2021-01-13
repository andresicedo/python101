'''
2. Matrix Addition
Given two two-dimensional lists of numbers of the size 2x2 
two dimensional list is represented as an list of lists:

[ [2, -2],
   [5, 3] ]
Calculate the result of adding the two matrices. The number in 
each position in the resulting matrix should be the sum of the 
numbers in the corresponding addend matrices. 

Example: to add

1 3
2 4
and

5 2
1 0
results in

6 5
3 4
'''
list_one = [[1, 2], [3,4]]
list_two = [[5,6], [7,8]]
one_atzero = list_one[0]
one_atone = list_one[1]
two_atzero = list_two[0]
two_atone = list_two[1]

one_one = list_one[1]
two_one = list_two[1]
print([one_atzero[0] + two_atzero[0], one_atone[1] + two_atone[1]],
[one_one[0] + two_one[0], one_one[1] + two_one[1]])