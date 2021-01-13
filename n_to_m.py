'''
8. n to m
Same as the previous problem, except you will prompt the user for 
the number to start on and the number to end on. Example session:

$ python3 n_to_m.py
Start from: 2
End on: 8
2
3
4
5
6
7
8
'''
while True:
    try:
        begin = int(input("Pick a number to begin with: "))
        end = int(input("Pick a number to end with: "))   
        while begin <= end:
            print(begin)
            begin = begin + 1
    except ValueError:
        print("Please enter a valid number!")
