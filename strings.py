'''
3. Find the shortest String
Write a function shortest that accepts a List of Strings as an argument.

It should return the shortest String in the List.

#4. Find the longest String
Write a function longest that accepts a List of Strings as an argument.

It should return the longest String in the List.

'''
def shortest(list):
    short_Str = list[0]
    for string in list:
        if len(short_Str) > len(string):
            short_Str = string
    return short_Str

output = shortest(["one-million", "three", "twenty-one"])
print(output)

def longest(list):
    long_Str = list[0]
    for string in list:
        if len(long_Str) < len(string):
            long_Str = string
    return long_Str

output = shortest(["one", "three", "twenty-one"])
print(output)