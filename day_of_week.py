'''
4. Day of the Week
Given the following code that prompts the user for a day number 
(Remember that the int function converts a numeric string to a number):

day = int(input('Day (0-6)? '))
# Fill in your code here
The user will enter a number from 0 to 6. Given this number, 
print a day of the week. 0 for Sunday, 1 for Monday, 2 for Tuesday, 
and so on. Here's an example user session (this assumes you've named 
the file day_of_week.py):

$ python3 day_of_week.py
Day (0-6)? 5
Friday
$ python day_of_week.py
Day (0-6)? 0
Sunday
'''
day = int(input('Day (0-6)? '))

if day == int("0"):
    print("Sunday")
elif day == int("1"):
    print("Monday")
elif day == int("2"):
    print("Tuesday")
elif day == int("3"):
    print("Wednesday")
elif day == int("4"):
    print("Thursday")
elif day == int("5"):
    print("Friday")
elif day == int("6"):
    print("Saturday")
else:
    print("Pick a day between 0-6!")
