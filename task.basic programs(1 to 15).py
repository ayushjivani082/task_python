

# Basic programs

1

print("Hello World")


2. 

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
print("sum =" , a + b)


3.

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
print("Difference =" , a - b)


4.

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
print("product =" , a * b)


5.

a = float(input("Enter numerator:"))
b = float(input("Enter second number:"))
if b != 0:
    print("Quotient =" , a / b)
else:
    print("cannot divide by zero")

6.

a = int(input("Enter dividend:"))
b = int(input("Enter divisor:"))
print("Remainder =" ,  a % b)


7.

n = float(input("Enter a number:"))
print("Square =" , n ** 2)


8.

n = float(input("Enter a number:"))
print("Cube =" , n ** 3)


9.

import math
r = float(input("Enter radius:"))
area = math.pi * r * r
print("Area =" , round(area , 2))


10.

P = float(input("Principal:"))
r = float(input("Rate of interest:"))
t = float(input("Time (years):"))

si = (P * r * t) / 100
print("Simple Interest =" , si)

11.

c = float(input("Celisus:"))
f = (c * 9/5) + 32
print("Fahrenheit =" , f)


12.

a = input("Enter first number :")
b = input("Enter second number :")
a , b = b , a
print("After swap -> a ="  , a, ",b =" , b)


13.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
avg = (a + b + c) / 3
print("Average =" , avg)


14.

m1 = float(input("Enter marks 1: "))
m2 = float(input("Enter marks 2: "))
m3 = float(input("Enter marks 3: "))
m4 = float(input("Enter marks 4: "))
m5 = float(input("Enter marks 5: "))
total = m1 + m2 + m3 + m4 + m5
percent = (total / 500) * 100
print("Total =" , total)
print("Percentange =" , percent)


15.

days = int(input("Enter days: "))
years = days // 365
months = (days % 365) // 30
remaining_days = (days % 365) % 30
print(f"Years: {years} , Months: {months} , Days: {remaining_days}")


