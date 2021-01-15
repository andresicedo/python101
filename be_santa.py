'''
Be Santa!
Write a program that simulates a visit to Santa,

--Ask the user what they want for Christmas (can be any number of items)
--Ask if they've been bad or good this year.
Based on their response, return the appropriate statement:
If they've been good, list the presents they'll receive.
If they've been bad, tell them they can expect a lump of coal.
Hints
Start with just a single item and make the script work. Then add more.
Use input to ask the user what they want, and assign the values to variables.
Use input to ask if they've been bad or good.
Use a conditional statement, if ... else, to determine the response.
Bonus
Involve Krampus!!
Add functions!
'''
input_one = input("Hello, what would you like for Christmas? ")
input_one_plus = input("Anything else? (y/n) ")
def santa(input_one, input_one_plus):
    if input_one_plus == 'y':
        gift = input("Whate else would you like? ")
        print("OK great!")
        input_two = input("Have you been 'bad' or 'good' this year? ")
        if input_two == "bad":
            return "Looks like you're on the naughty list this year...\nA lump of coal and visit from Krampus it is."
        else:
            return f"You're going to have a great Christmas this year with a {input_one} and {gift}!"
    else:
        input_two = input("Have you been 'bad' or 'good' this year? ")
        if input_two == "bad":
            return "Looks like you're on the naughty list this year...\nA lump of coal and visit from Krampus it is."
        else:
            print("OK great!")
            return f"You're going to have a great Christmas this year with a {input_one}!"
output = santa(input_one, input_one_plus)
print(output)

    