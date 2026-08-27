from datetime import datetime , timedelta

now = datetime.now()

print("Today's date: " , now.date())
print("Current time: " , now.date())

future_date = now + timedelta(days=30)

print("Date after 30 days: " , future_date.date())



import random

for i in range(5):
    dice1 = random.randint(1 , 6)
    dice2 = random.randint(1 , 9)
    total = dice1 + dice2
    print(f"Roll {i+1}: {dice1} + {dice2} = {total}")



import random
import string

characters = string.ascii_letters + string.digits

password = ''.join(random.choice(characters) for i in range(8))

print("Random Password: " , password)



import math

number = float(input("Enter a number: "))

print("square root:" , math.sqrt(number))
print("Ceiling:" , math.ceil(number))
print("Floor:" , math.floor(number))
print("Log:" , math.log(number))
      




import uuid

for i  in range(3):
    unique_id = uuid.uuid4()
    print(f"Unique ID {i+1}: {unique_id}")




from functools import reduce
number = [1 , 2 , 3 , 4 , 5]
# Double all numbers
doubled = list(map(lambda x: x * 2, number))
# Keep even numbers
evens = list(filter(lambda x: x % 2 == 0, number))
# Find product
product = reduce(lambda x , y: x * y , number)

print("Original:" , number)
print("Double:" , doubled)
print("Even numbers:" , evens)
print("Product:" , product)





File: utils.py
def greet(name):
    return "Hello " + name
def square(number):
    return number * number
def add(a , b):
    return a + b

File: main.py
import utils
print(utils.greet("Ayush"))
print("Square: " , utils.square(5))
print("Addition: " , utils.add(10 , 20))












