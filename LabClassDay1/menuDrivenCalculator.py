x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))
while True:
    menu = int(input("1.Add \n2. Subtract \n3. Multiply \n4. Division \n5. Quit\nEnter option number: \n>>>"))
    if menu == 1:
        print(x+y)
    elif menu == 2:
        print(x-y)
    elif menu == 3:
        print(x*y)
    elif menu == 4:
        print(x/y)
    elif menu == 5:
        quit()
    else:
        print("Invalid option.")

