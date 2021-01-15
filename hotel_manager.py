'''
Hotel Manager
Imagine that you're running a hotel, and you want to keep track of guests by floor and room number. 
Start with the following dictionary:
Write a program that does the following:


Additional Rules:

Do not allow anyone to check into a room that is already occupied!
Do not allow checking out of a room that isn't occupied!
Hints
Start by writing down (analog style, pen & paper, or in a text file) all the steps you think a 
user will need to go through.
Use input to ask the user for their status (checking in/out), number of occupants, floor, and 
room numbers.
Use functions to break up your programs behaviors based on the responses.
Functions should encapsulate the steps you outlined earlier.
Examples might include:
Checking In
Checking Out
Assigning a room and floor during check in
Clearing a room after check out
Use while loops and conditionals, if...else to determine if a room is available or not.
For example while occupants > 0 ...
Start with just adding a single occupant to a room, then add more.
A combination of a for loop and the range() function might be helpful when collecting a list 
of occupants names. https://pynative.com/python-range-function/
Bonus
Limit the max number of occupants in a room to 6.
Loop the program so that it goes back to the first question after displaying a list of all the occupants.
Import Python's pprint module for printing out the list of occupants. 
https://docs.python.org/3/library/pprint.html
'''

hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}
# Display a menu asking whether to check in or check out.
menu = input("Hello! What would you like to do? \nCheck In\nCheck Out\n")
# Prompt the user for a floor number, then a room number.
# If checking in, ask for the number of occupants and what their names are.
if menu == 'Check In' or 'Check In'.lower():
    floor = int(input(f"What floor? {hotel.keys()}\n"))
    if floor == 1:
        floor_one = '100-199'
        room = int(input(f"What room number? {floor_one}\n"))
        while hotel[f"{floor}"][f"{room}"]:
            print("ROOM OCCUPIED!\nPlease pick a different floor")
            room = int(input(f"What room number? {floor_one}\n"))
            break
    if floor == 2:
        floor_one = '200-299'
        room = int(input(f"What room number? {floor_one}\n"))
        while hotel[f"{floor}"][f"{room}"]:
            print("ROOM OCCUPIED!\nPlease pick a different floor")
            room = int(input(f"What room number? {floor_one}\n"))
            break
    if floor == 3:
        floor_one = '300-399'
        room = int(input(f"What room number? {floor_one}\n"))
        while hotel[f"{floor}"][f"{room}"]:
            print("ROOM OCCUPIED!\nPlease pick a different floor")
            room = int(input(f"What room number? {floor_one}\n"))
            break
    occupants = int(input("How many occupants will be checking in?\n"))
    if occupants == 1:
        name = input("May I please have your name? ")
        hotel[f"{floor}"][f"{room}"] = name
        print("Current Occupants: ", hotel)
    if occupants == 2:
        print("May I please have your names? ")
        name1 = input("Name 1: ")
        name2 = input("Name 2: ")
        hotel[f"{floor}"][f"{room}"] = [name1, name2]
        print(hotel)
    if occupants == 3:
        print("May I please have your names? ")
        name1 = input("Name 1: ")
        name2 = input("Name 2: ")
        name3 = input("Name 3: ")
        hotel[f"{floor}"][f"{room}"] = [name1, name2, name3]
        print("Thank you for checking in!")
        print(hotel)
# If checking out, remove the occupants from that room.
if menu == 'Check Out' or "Check Out".lower():
    room = input("What room number? \n")
    print("Thank you for staying with us!")
    del hotel[floor][room]
    print(hotel)
# After checking in or out, display a list of all the occupants and their rooms.