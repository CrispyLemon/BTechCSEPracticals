def gen_fib(n):
    a, b = 0, 1
    while a < n:
        yield a 
        a,b = b, a+b

x = int(input("How many terms do you want to generate? \n>>> "))

y  = gen_fib(x)
for i in y:
    print(i)