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
def registration(menu):
  if menu == 1:
    floor = int(input(f"What floor? {hotel.keys()}\n"))
    if floor == 1:
      rooms = '100-199'
      room = input(f"What room number? {rooms}\n")
    if floor == 2:
      rooms = '200-299'
      room = input(f"What room number? {rooms}\n")
    if floor == 3:
      rooms = '300-399'
      room = input(f"What room number? {rooms}\n")
    while floor is not 1 or 2 or 3:
      print("We only have 3 floors at the hotel. \nPlease enter a valid floor\n")
      return registration(menu)  
    for occupied in hotel[f"{floor}"]:
      while occupied == room:
        print("ROOM OCCUPIED!\nPlease pick a different room")
        room = input(f"What room number? {rooms}\n")
        while occupied == room:
          print("ROOM OCCUPIED!\nPlease pick a different room")
          room = input(f"What room number? {rooms}\n")
          while occupied == room:
            print("ROOM OCCUPIED!\nPlease pick a different room")
            return registration(menu)
        break
    occupants = int(input("How many guests will be checking in?\n"))  
    if occupants == 1:
      name = input("May I please have your name? ")
      hotel[f"{floor}"][f"{room}"] = [name]
      print(f"Thank you for checking in {name}!\nYou are in room {room}!")
      print(f"Current Occupants:\n")
      for key,value in hotel.items():
        print(key, value)
    if occupants == 2:
      print("May I please have your names? ")
      name1 = input("Name 1: ")
      name2 = input("Name 2: ")
      hotel[f"{floor}"][f"{room}"] = [name1, name2]
      print(f"Thank you for checking in {name1} and {name2}!\nYou are in room {room}!")
      print(f"Current Occupants:\n")
      for key,value in hotel.items():
        print(key, value)
    if occupants == 3:
      print("May I please have your names? ")
      name1 = input("Name 1: ")
      name2 = input("Name 2: ")
      name3 = input("Name 3: ")
      hotel[f"{floor}"][f"{room}"] = [name1, name2, name3]
      print(f"Thank you for checking in {name1}, {name2} and {name3}!\nYou are in room {room}!")
      print(f"Current Occupants:\n")
      for key,value in hotel.items():
        print(key, value)
    if occupants == 4:
      print("May I please have your names? ")
      name1 = input("Name 1: ")
      name2 = input("Name 2: ")
      name3 = input("Name 3: ")
      name4 = input("Name 4: ")
      hotel[f"{floor}"][f"{room}"] = [name1, name2, name3, name4]
      print(f"Thank you for checking in {name1}, {name2}, {name3} and {name4}!\nYou are in room {room}!")
      print(f"Current Occupants:\n")
      for key,value in hotel.items():
        print(key, value)
    if occupants == 5:
      print("May I please have your names? ")
      name1 = input("Name 1: ")
      name2 = input("Name 2: ")
      name3 = input("Name 3: ")
      name4 = input("Name 4: ")
      name5 = input("Name 5: ")
      hotel[f"{floor}"][f"{room}"] = [name1, name2, name3, name4, name5]
      print(f"Thank you for checking in {name1}, {name2}, {name3}, {name4} and {name5}!\nYou are in room {room}!")
      print(f"Current Occupants:\n")
      for key,value in hotel.items():
        print(key, value)
    if occupants == 6:
      print("May I please have your names? ")
      name1 = input("Name 1: ")
      name2 = input("Name 2: ")
      name3 = input("Name 3: ")
      name4 = input("Name 4: ")
      name5 = input("Name 5: ")
      name6 = input("Name 6: ")
      hotel[f"{floor}"][f"{room}"] = [name1, name2, name3, name4, name5, name6]
      print(f"Thank you for checking in {name1}, {name2}, {name3}, {name4}, {name5} and {name6}!\nYou are in room {room}!")
      print(f"Current Occupants:\n")
      for key,value in hotel.items():
        print(key, value)
    while occupants > 6:
      print("The hotel only allows a maximum of 6 guests per room.\nConsider getting a second room.\n")
      return registration(menu)
  if menu == 2:
    floor = int(input(f"What floor? {hotel.keys()}\n"))
    occupied = hotel[str(floor)].keys()
    room = input(f"Choose your room on floor {floor}? \nOccupied rooms: {occupied}\n")
    if room not in occupied:
      print("Invalid room number!\nPlease try again.")
      room = input(f"Choose your room on floor {floor}? \nOccupied rooms: {occupied}\n")
    name = input("May I please have your name? ")
    if name in hotel[str(floor)][room]:
      print(f"Thank you for staying with us {name}!")
      print(f"You have been checked out of room {room}!")
      del hotel[str(floor)][room]
      print(f"Current Occupants:\n")
      for key,value in hotel.items():
        print(key, value)
    else:
          print("I'm sorry I don't have you registered as a guest.")
          name = input("Please entere the registered guest name: ")
          for name in hotel[str(floor)][room]:
            if hotel[str(floor)][room].index(name) > -1:
              print(f"Thank you for staying with us {name}!")
              del hotel[str(floor)][room]
              print(f"Current Occupants:\n")
              for key,value in hotel.items():
                print(key, value)
  while menu != 1 or 2:
    registration(int(input("What else would you like to do? \n1) Check In\n2) Check Out\n")))

while True:
  registration(int(input("What else would you like to do? \n1) Check In\n2) Check Out\n")))

output = registration(int(input("Hello! What would you like to do? \n1) Check In\n2) Check Out\n")))
print(output)
