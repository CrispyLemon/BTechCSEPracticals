#write a program to print the fibonacci series using recursion

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n = int(input("Enter the number of terms: "))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i), end=" ")

# Output:
# Enter the number of terms: 10
# Fibonacci sequence:
# 0
# 1
# 1

