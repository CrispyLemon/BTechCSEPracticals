#write a program to multiply two matrices using (i) arrays by using lists  (ii) numpy arrays

#using lists

#defining function to multiply matrices

def matrixMult(list1, list2):
    list3 = []
    for i in range(len(list1)):
        list3.append([])
        for j in range(len(list2[0])):
            list3[i].append(0)
            for k in range(len(list2)):
                list3[i][j] += list1[i][k] * list2[k][j]
    return list3

#taking input from user
row1 = int(input("Enter the number of rows of the first matrix: "))
col1 = int(input("Enter the number of columns of the first matrix: "))
row2 = int(input("Enter the number of rows of the second matrix: "))
col2 = int(input("Enter the number of columns of the second matrix: "))
list1 = []
list2 = []

#taking input for first matrix
print("Enter the elements of the first matrix: ")

for i in range(row1):
    list1.append([])
    for j in range(col1):
        list1[i].append(int(input(f"Enter the element of the first matrix at ({i},{j}): ")))

#taking input for second matrix
print("Enter the elements of the second matrix: ")

for i in range(row2):
    list2.append([])
    for j in range(col2):
        list2[i].append(int(input(f"Enter the element of the second matrix at ({i},{j}): ")))

#calling function to multiply matrices
list3 = matrixMult(list1, list2)

#displaying result
print("The result of the multiplication is: ")
for i in range(len(list3)):
    for j in range(len(list3[0])):
        print(list3[i][j], end=" ")
    print()

#using numpy arrays

#importing numpy
import numpy as np

#defining function to multiply matrices

def matrixMult(list1, list2):
    list3 = np.zeros((len(list1), len(list2[0])))
    for i in range(len(list1)):
        for j in range(len(list2[0])):
            for k in range(len(list2)):
                list3[i][j] += list1[i][k] * list2[k][j]
    return list3

#taking input from user
row1 = int(input("Enter the number of rows of the first matrix: "))
col1 = int(input("Enter the number of columns of the first matrix: "))
row2 = int(input("Enter the number of rows of the second matrix: "))
col2 = int(input("Enter the number of columns of the second matrix: "))
list1 = []
list2 = []

#taking input for first matrix
print("Enter the elements of the first matrix: ")

for i in range(row1):
    list1.append([])
    for j in range(col1):
        list1[i].append(int(input(f"Enter the element of the first matrix at ({i},{j}): ")))

#taking input for second matrix
print("Enter the elements of the second matrix: ")

for i in range(row2):
    list2.append([])
    for j in range(col2):
        list2[i].append(int(input(f"Enter the element of the second matrix at ({i},{j}): ")))

#calling function to multiply matrices
list3 = matrixMult(list1, list2)

#displaying result
print("The result of the multiplication is: ")
for i in range(len(list3)):
    for j in range(len(list3[0])):
        print(list3[i][j], end=" ")
    print()
