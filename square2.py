'''
10. Print a Square II
Print a NxN square of * characters. Prompt the user for N. Example output:

$ python3 square2.py
How big is the square? 10
**********
**********
**********
**********
**********
**********
**********
**********
**********
**********
'''
side = int(input("Enter the size of your square: "))
i = 0

while(i < side):
    j = 0
    while(j < side):      
        j = j + 1
        print("*", end = '  ')
    i = i + 1
    print()