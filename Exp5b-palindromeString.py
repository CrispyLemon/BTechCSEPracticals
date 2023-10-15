def paliString():
    x = input("Enter string to check: ")
    tempString=""
    for i in range((len(x)-1),-1,-1):
        tempString = tempString + x[i]
    if tempString == x:
        return f"String {x} is a palindrome."
    return f"String {x} is not a palindrome."

print(paliString())