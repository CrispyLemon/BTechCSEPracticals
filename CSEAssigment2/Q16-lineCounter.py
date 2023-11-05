#create a python program that reads a text file line by line and counts the number of lines in the file.


def lineCounter(fileName):
    count = 0
    with open(fileName, 'r') as f:
        for line in f:
            count += 1
    return count

print(lineCounter("file.txt"))

