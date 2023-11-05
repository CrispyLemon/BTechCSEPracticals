#define a class complexNumbers. write methods for addition, subtraction, multiplication using the notion of operator overloading

class complexNumbers:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return complexNumbers(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return complexNumbers(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return complexNumbers(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
#taking input from user

real1 = int(input("Enter the real part of the first complex number: "))
imag1 = int(input("Enter the imaginary part of the first complex number: "))
real2 = int(input("Enter the real part of the second complex number: "))
imag2 = int(input("Enter the imaginary part of the second complex number: "))
num1 = complexNumbers(real1, imag1)
num2 = complexNumbers(real2, imag2)

#displaying result
print("The sum of the two complex numbers is: ", num1 + num2)
print("The difference of the two complex numbers is: ", num1 - num2)
print("The product of the two complex numbers is: ", num1 * num2)

