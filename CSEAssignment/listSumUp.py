def listSumUp():
    x = eval(input("Enter a list (with enclosing brackets): "))
    temp = list()
    sum = 0
    for i in range(0, len(x)):
        sum += int(x[i])
        temp.append(sum)
    return temp

print(listSumUp())
        