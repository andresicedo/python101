'''
2. Celsius to Fahrenheit conversion
The formula to convert a temperature from Celsius to Fahrenheit is:

F = (C * 9/5) + 32

Write a function that takes a temperature in Celsius, converts 
it Fahrenheit, and returns the value.
'''
def conversion(C):
    F = (C * (9 / 5)) + 32
    return F
temperature = conversion(-5)
print(f"{temperature} F")

'''
3. Fahrenheit to Celsius conversion
The formula to convert a temperature from Fahrenheit to Celsius is:

C = (F - 32) * 5/9

Write a function that takes a temperature in Fahrenheit, 
converts it to Celsius, and returns the value.

'''
def convert(F):
    C = float(round((F - 32) * (5 / 9)))
    return C
temperature = convert(85)
print(f"{temperature} C")