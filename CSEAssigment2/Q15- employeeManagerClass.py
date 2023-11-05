#create an employee class. extend the employee class. derive a class manager from the employee class so that it lists the details of manager as well as the details of the employees working under that manager.

class Employee:
    def __init__(self, name, age, salary, designation):
        self.name = name
        self.age = age
        self.salary = salary
        self.designation = designation

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nSalary: {self.salary}\nDesignation: {self.designation}"
    
class Manager(Employee):
    def __init__(self, name, age, salary, designation, employees):
        super().__init__(name, age, salary, designation)
        self.employees = employees

    def __str__(self):
        return f"{super().__str__()}\nEmployees: {self.employees}"
    
emp1 = Employee("John", 25, 25000, "Software Engineer")
emp2 = Employee("Jane", 23, 20000, "Software Engineer")
emp3 = Employee("Jack", 27, 30000, "Software Engineer")
print(emp1, "\n", emp2, "\n", emp3)
manager = Manager("James", 30, 50000, "Manager", [emp1, emp2, emp3])
print(manager)


