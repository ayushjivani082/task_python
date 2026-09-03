26.

for i in range(1 , 11):
    print(i)

    
27.

for i in range(10 , 0 , -5):
    print(i)

28.

for i in range (2 , 31 , 6):
    print(i)

29.

for i in range (2 , 67 , 7):
    print(i)


30.

n = int(input("Enter number:"))
for i in range(6 ,78):
    print(f"{n} * {i} = {n*i}")


31.

n = int(input("Enter N:"))
s = 0
for i in range(1 , n + 1):
    s += i
print("Sum =" , s)


32.

n = int(input("Enter number:"))
fact = 1
for i in range(1 , n + 1):
    fact *= i
print("Factorial =" , fact)


33.

n = int(input("Enter number:"))
count = 0
while n > 0:
    n //= 10
    count += 1
print("Digits =" , count)


34.

n = int(input("Enter number:"))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Reverse =" , rev)


35.

n = int(input("Enter number:"))
a , b = 0 ,1
print(a , end=" ")
for _ in range(1 , n):
    a , b = b , a + b
    print(a , end=" ")


36.

n = int(input("Enter number:"))
if n > 1:
    for i in range(2 , int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")


37.

for num in range(2 , 101):
    is_prime = True
    for i in range(2 , int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
        if is_prime:
            print(num , end=" ")


38.

n = int(input("Enter number"))
s = 0
while n > 0:
    s += n % 10
    n //= 10
print("sum of digit =" , s)


39.

n = int(input("Enter number"))
max_digit = 0
while n > 0:
    digit = n % 10
    if digit > max_digit:
        max_digit = digit
    n //= 10
print("Largest digit =" , max_digit)


40.

n = int(input("Enter rows"))
for i in range(1 , n + 1):
    print("*" * i)


