file = open("data.txt" , "w")
file.write("Python is easy.\n")
file.write("I am lerning Python.\n")
file.write("Python is a programming language.\n")
file.write("I like coding.\n")
file.write("practice makes programming better.\n")
file.close()

file = open("data.txt" , "r")
for line in file:
    print(line , end="")
file.close()    



try:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Result: " , result)
except ZeroDivisionError:
    print("Error: cannot division by Zero.")
except ValueError:
    print("Error: Please enter valid numbers.")




file = None
try:
    file = open ("data.txt" , "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    if file:
        file.close()
        print("File closed.")

        


class AgeError(Exception):
    pass
try:
    age = int(input("Enter your age: "))
    if age < 0 or age > 150:
        raise AgeError("Age must be between 0 and 150.")
    print("Valid age:" , age)
except AgeError as e:
    print("AgeError: " , e)
except ValueError:
    print("Please enter a valid number.")




try:
    file = open("data.txt" , "r")
    text = file.read()
    words = text.split()
    print("Total words: " , len(words))
    file.close()
except FileNotFoundError:
    print("File closed.")



def cheak_positive(number):
    assert number > 0 , "Number must be positive."
    print("Valid positive number: " , number)
    
try:
    num = float(input("Enter a number: "))
    cheak_positive(num)
except AssertionError as e:
    print("Error: " , e)







        
