import operators, math, random


print(operators.add(10,9))

print(random.randint(8))
while True:
    x = random.randint(0,10)
    guess = int(input("Guess a number between 0 and 10. \n>>> "))
    if guess == x:
        print("You guessed right.")
    y = input("Continue? \n>>> ")
    if y in 'nN':
        break