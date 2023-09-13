def stringReverser(x):
    reverse = ""
    for i in range(len(x)-1,-1,-1):
        reverse += x[i]
    return reverse

print(stringReverser(input("Enter a sentence: ")))
