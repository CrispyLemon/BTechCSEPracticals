#Write a function that takes as input a string and returns the string after deleting all the vowels, Use at least three ways to implement.

def vowelDelete1(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in string.lower():
        if x in vowels:
            string = string.replace(x, "")
    return string

def vowelDelete2(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in vowels:
        string = string.replace(x, "")
    return string

def vowelDelete3(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    result = ""
    for x in string:
        if x not in vowels:
            result += x
    return result

#sample cases of each function
print(vowelDelete1("Hello World"))
print(vowelDelete2("Hello World"))
print(vowelDelete3("Hello World"))

