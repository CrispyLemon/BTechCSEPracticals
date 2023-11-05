#write a program to use dictionaries to store and retrieve student grades

# Create a dictionary

studentDictionary = {}

# Add students and their grades to the dictionary using user input  user defined number of times and for loop
# check if the student already exists in the dictionary
# if the student exists in the dictionary, print the student name and grade
# if the student does not exist in the dictionary, add the student name and grade

for i in range(int(input("Enter the number of students: "))):
    studentName = input("Enter the name of the student: ")
    studentGrade = input("Enter the grade of the student: ")
    if studentName in studentDictionary:
        print("Student already exists")
        print(studentName, studentDictionary[studentName])
    else:
        studentDictionary[studentName] = studentGrade
        print("Student added to the dictionary")


# Display the dictionary using student name as index taken from user input and if the student does not exist, display a message
while True:
    print(studentDictionary.get(input("Enter the name of the student to display the grade: "), "Student does not exist"))
    if input("Do you want to continue? (y/n): ") == "n":
        break
