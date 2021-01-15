'''
Validate Subsequence
What is a subsequence? A subsequence is an array (set of numbers) that 
aren't necessarily adjacent in the array but are in the same order as 
the original sequence.
##Examples: Array - [1,2,3,4,5] Subsequence- [2,3,4] #This is a 
# subsequence because even though it doesn't contain all the numbers that 
# #The original sequence has, it does contain some of the values in the 
# exact same order.

Example:

print(isValidSubsequence([1,2,3,4], [2,4])) => True
#Why? Even though it doesn't have all the values, it has the same ones in the same order.
print(isValidSubsequence([1,2,3,4], [4, 2])) => False
#Why? Even though the subsequence has values that match values in the array, it is not in the same order.
Headstart:

def isValidSubsequence(array, sequence): 
#make sure to add both array and sequence as arguements.
'''
def isValidSubsequence(array, sequence): 
    if :
        return True
    else:
        return False

print(isValidSubsequence([1,2,3,4], [2,4])) # True
print(isValidSubsequence([1,2,3,4], [4, 2])) # False