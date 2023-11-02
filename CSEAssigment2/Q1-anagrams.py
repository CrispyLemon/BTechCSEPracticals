def anagram(a,b):

    str1 = sorted("".join(tuple(a.split())))
    str2 = sorted("".join(tuple(b.split())))
    
    if str1 == str2:
        return True
    else:
        return False

x = input("Enter a string: ")
y = input("Enter an anagram: ")

print(anagram(x,y))
