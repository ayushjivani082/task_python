def greeting(name , age):
    return f"Hello {name}! You are {age} years old."

#Example
print(greeting("Ayush" , 20))



def calculate_sum(*args):
    return sum(args)

#Example
print(calculate_sum(10 , 20 , 30 , 40 , 50))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example
print(factorial(5))


students = [("Ayush" , 89) , ("Man" , 90) , ("Kushal" , 78) , ("Ved" , 88)]

sorted_students = sorted(students , key=lambda x: x[1])
print(sorted_students)


array = [10 , 20 , 30 , 40 , 50 , 60]
# Insert on element
array.insert(2 , 25)
#delete on element
array.remove(50)
#search on element
element = 30
if element in array:
    print(element , "found in the array")
else:
    print(element , "not found in the array")

print("finl array:" , array)


matrix = [
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7 , 8 , 9]
]

for row in matrix:
    print(row)



students = ["Ayush" , "Ved" , "Man" , "prit" , "Amit"]
marks = [78 , 78 , 90 , 67 , 78]

students.sort()               #Alphabetical order
marks.sort(reverse = True)    #Descendind order

print("Students: " , students)
print("Marks: " , marks)


def report_card(**kwargs):
    print("-----REPORT CARD-----")
    for key , value in kwargs.items():
        print(f"{key} : {value}")


#Example
report_card(
    Name = "Ayush",
    Age = 20,
    python = 90,
    SQL = 98,
    Maths = 99,
    total = 287
)    
    

    

      


