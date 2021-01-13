'''
5. Work or Sleep In?
Prompt the user for a day of the week just like the previous problem. 
But this time, print "Go to work" if it's a work day and "Sleep in" 
if it's a weekend day. Example session:

$ python3 work_or_sleep_in.py
Day (0-6)? 5
Go to work
$ python work_or_sleep_in.py
Day (0-6)? 6
Sleep in
'''
day = input('Day (0-6)? ')

if day == ("0"):
    print("Sleep in")
elif day == ("1"):
    print("Go to work")
elif day == ("2"):
    print("Go to work")
elif day == ("3"):
    print("Go to work")
elif day == ("4"):
    print("Go to work")
elif day == ("5"):
    print("Go to work")
elif day == ("6"):
    print("Sleep in")
else:
    print("Pick a valid number")