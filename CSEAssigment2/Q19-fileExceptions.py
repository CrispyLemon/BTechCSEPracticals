#Write a python program to Handle exceptions for file operations and input validation.

def fileRead(fileName):
    try:
        with open(fileName, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("File does not exist")
        return ""
    except:
        print("Unknown error")
        return ""
    
def fileWrite(fileName, content):
    try:
        with open(fileName, 'w') as f:
            f.write(content)
    except:
        print("Unknown error")

while True:
    ch = int(input("1. Read file\n2. Write to file\n3. Exit\nEnter your choice: "))
    if ch == 1:
        fileName = input("Enter file name: ")
        print(fileRead(fileName))
    elif ch == 2:
        fileName = input("Enter file name: ")
        content = input("Enter content: ")
        fileWrite(fileName, content)
    elif ch == 3:
        break
    else:
        print("Invalid choice") 