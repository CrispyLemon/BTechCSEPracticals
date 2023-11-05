#WAP to find the largest word in a file.

def longestWord(fileName):
    longest = ""
    with open(fileName, 'r') as f:
        for line in f:
            for word in line.split():
                if len(word) > len(longest):
                    longest = word
    return longest

print(longestWord("file.txt"))

