#write a python program to test the seek and tell methods of file objects.

def seekTellTester(fileName):
    with open(fileName, 'r') as f:
        print(f.tell())
        print(f.read(5))
        print(f.tell())
        print(f.read(5))
        print(f.tell())
        print(f.read(5))
        print(f.tell())
        f.seek(0)
        print(f.tell())
        print(f.read(5))
        print(f.tell())
        print(f.read(5))
        print(f.tell())
        print(f.read(5))
        print(f.tell())
        f.seek(10)
        print(f.tell())
        print(f.read(5))
        print(f.tell())
        print(f.read(5))
        print(f.tell())
        print(f.read(5))
        print(f.tell())
        f.seek(0, 2)
        print(f.tell())
        print(f.read(5))
        print(f.tell())
        print(f.read(5))
        print(f.tell())
        print(f.read(5))
        print(f.tell())
        f.seek(0, 1)
        print(f.tell())
        print(f.read(5))
        print(f.tell())
        print(f.read(5))
        print(f.tell())
        print(f.read(5))
        print(f.tell())
        f.seek(0, 0)
        print(f.tell())
        print(f.read(5))
        print(f.tell())
        print(f.read(5))
        print(f.tell())
        print(f.read(5))
        print(f.tell())

seekTellTester("file.txt")
