name = "Ayush"
age = 18
city = "surat"

print("Nmae :" , name)
print("Age : " , age)
print("City : " , city)



name = input("Enter your name : ")
print("Hello ," , name + " ! Welcome to python ! ")


age = 18
height = 5.8
name = "Ayush"
is_student = True

print("Age : " , age, type(age))
print("Height : " , height, type(height))
print("Nmae : " , name, type(name))
print("Is_student : " , is_student, type(is_student))


a = 10
b = 6

print("ID of a : " , id(a))
print("ID of b : " , id(b))

if id(a) == id(b) :
    print("Both variable point to the same memory.")

else :
    print("Variablr point to different memory.")


a = float(input("Enter your first number : "))
b = float(input("Enter your second number : "))

print("Addition : " , a + b)
print("Subtraction : " , a - b)
print("Multiplication : " , a * b)
print("Division : " , a / b)
print("floor Division : " , a // b)
print("Modulus : " , a % b)
print("Exponent : " , a ** b)


# Float to int
a = 10.5
b = int(a)


# Int to string
c = 25
d = str(c)

# String to float
e = "15.5"
f = float(e)

print("Float to Int : " , b)
print("Int to String : " , d)
print("String to Float : " , f)



celsius =float(input("Enter temperature in Celsius : "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit : " , fahrenheit)
































          
