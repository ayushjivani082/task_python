41.

i = 1
while i <= 10:
    print(i)
    i += 1


42.

i = 2
while i <= 20:
    print(i)
    i += 2


43.

i = 1
while i <= 20:
    print(i)
    i += 2


44.

n = int(input("Enter number:"))
i = 1
fact = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial =" , fact)


45.

n = int(input("Enter number:"))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Reverse =" , rev)


46.

n = int(input("Enter number:"))
s = 0
while n > 0:
    s += n % 10
    n //= 10
print("Sum of digit =" , s)

47.

n = int(input("Enter number:"))
count = 0
while n > 0:
    n //= 10
    count += 1
print("Digits =" , count)

48.

import random
num = random.randint(1 , 100)
print("Guess a number between 1 and 100")
while True:
    guess = int(input("Enter your guess:"))
    if guess < num:
        print("Too low! Try again.")
    elif guess > num:
        print("Too high! Try again.")
    else:
        print("Congratulation! you guessed it.")
        break


49.

while True:
    print("\nMenu: 1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")
    choice = input("Enter choice:")
    if choice == '5':
        print("Thank you!")
        break
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    if choice == '1':
        print("Result =" , a + b)
    elif choice == '2':
        print("Result =" , a - b)
    elif choice == '3':
        print("Result = " , a * b)
    elif choice == '4':
        if b != 0:
            print("Result =" , a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid choice")



50.

while True: 
    n = int(input("Enter a number (0nto stop):"))
    if n == 0:
        print("you entered 0. program stopped.")
        break
    else:
        print("You entered:" , n)
