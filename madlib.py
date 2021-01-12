'''
3. Madlib
Prompt the user for the missing words to a Madlib sentence using 
the input function. You can make up your own Madlib sentence, 
but here's an example:

____(name)____'s favorite subject in school is ____(subject)____.
With the above given sentence, this is what a user session might look like:

$ python3 madlib.py
Please fill in the blanks below:
____(name)____'s favorite subject in school is ____(subject)____.
What is name? Marty
What is subject? time travel
Marty's favorite subject in school is time travel.
'''

print("Please complete the song!!!")
Guess_1 = input("Jingle ____ ")
Guess_2 = input("Jingle ____ ")
Guess_3 = input("Jingle all the ___ ")
Guess_4 = input("Oh, what ___ ")
Guess_5 = input("it is to ____ ")
Guess_6 = input("In a one _____ ")
Guess_7 = input("open _____ ")


madlib = f"Jingle {Guess_1}, jingle {Guess_2}, /Jingle all the {Guess_3}/Oh, what {Guess_4} it is to {Guess_5}/In a one {Guess_6} open {Guess_7}!"

print(madlib)

if madlib == "Jingle bells, jingle bells, /Jingle all the way/Oh, what fun it is to ride/In a one horse open sleigh!":
    print("You did it!")
else:
    print("Sorry, please try again!")