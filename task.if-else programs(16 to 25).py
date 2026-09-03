16.

n = float(input("Enter a number:"))
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")


17.

n = int(input("Enter a number :"))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")


18.

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
if a > b:
    print("Largest =" , a)
elif b > a:
    print("Largest =" , b)
else:
    print("Both are equal")

    
19.

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
c = float(input("Enter third number:"))
if a >= b and a >= c:
    print("Largest =" , a)
elif b >= a and b >= c:
    print("Largest =" , b)
else:
    print("Largest =" , c)


20.

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
c = float(input("Enter third number:"))
if a <= b and a <= c:
    print("Smallest =" , a)
elif b  <= a and b <= c:
    print("Smallest =" , b)
else:
    print("Smallest =" , c)


21.

age = int(input("Enter your age:"))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


22.

year = int(input("Enter year:"))
if (year % 4 == 0 and year  % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


23.

ch = input("Enter a character:").lower()
if ch in 'aeiou':
    print("Vovel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not a vaild alphabet")


24.

n = int(input("Enter a number:"))
if n % 5 == 0:
    print("divisible by 5")
else:
    print("Not divisible by 5")


25.

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
op = input("Enter operator (+ , - , * , /):")
if op == '+':
    print("Result =" , a + b)
elif op == '-':
    print("Result =" , a -b)
elif op == '*':
    print("Result =" , a * b)
elif op == '/':
    if b != 0:
        print("Rsult =" , a/b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
    
    
