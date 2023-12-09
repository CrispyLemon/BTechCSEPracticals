#implement string operations (e.g concentation, substring, length, etc.) using python

#concatenation  
str1 = "Hello"
str2 = "World"
str3 = str1 + str2
print(str3)

#substring
str4 = str3[0:5]
print(str4)

#length
print(len(str3))

#lowercase  
print(str3.lower())

#uppercase
print(str3.upper())

#replace
print(str3.replace("World", "Universe"))

#split
print(str3.split(" "))

#strip
str5 = "   Hello World   "
print(str5.strip())

