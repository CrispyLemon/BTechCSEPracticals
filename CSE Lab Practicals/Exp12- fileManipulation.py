#read data from a text file and perform operations

# 1. Write a Python program to read an entire text file.
# 2. Write a Python program to read first n lines of a file.
# 3. Write a Python program to append text to a file and display the text.  
# 4. Write a Python program to read last n lines of a file.

# 5. Write a Python program to read a file line by line and store it into a list.
# 6. Write a Python program to read a file line by line store it into a variable.
# 7. Write a Python program to read a file line by line store it into an array.

# 8. Write a Python program to count the number of lines in a text file.
# 9. Write a Python program to count the frequency of words in a file.

# 10. Write a Python program to get the file size of a plain file.
# 11. Write a Python program to write a list to a file.
# 12. Write a Python program to copy the contents of a file to another file .

# 1
with open("file.txt", 'r') as f:
    print(f.read())

# 2
with open("file.txt", 'r') as f:
    print(f.read(5))

# 3
with open("file.txt", 'a') as f:
    f.write("This is a new line\n")
    f.write("This is another new line\n")
    f.write("This is yet another new line\n")
    f.write("This is the last new line\n")

with open("file.txt", 'r') as f:
    print(f.read())

# 4
with open("file.txt", 'r') as f:
    x = int(input("Enter lines:"))
    print(f.readlines()[-x:])

# 5
with open("file.txt", 'r') as f:
    print(f.readlines())

# 6
with open("file.txt", 'r') as f:
    print(f.read())

# 7
with open("file.txt", 'r') as f:
    print(f.read().split('\n'))

# 8
with open("file.txt", 'r') as f:
    print(len(f.readlines()))

# 9
with open("file.txt", 'r') as f:
    print(f.read().split())

# 10
import os
print(os.stat("file.txt").st_size)

# 11
with open("file.txt", 'r') as f:
    print(f.read().split())

# 12
with open("file.txt", 'r') as f:
    with open("file2.txt", 'w') as f2:
        f2.write(f.read())

with open("file2.txt", 'r') as f:
    print(f.read())
