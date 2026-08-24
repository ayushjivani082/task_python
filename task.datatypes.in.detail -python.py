sentence = input("Enter a sentence: ")
vowels= 0
consonants = 0
spaces = 0

for char in sentence:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char ==" ":
        spaces += 1

words = len(sentence.split())

print("Vowels: " , vowels)
print("Consonants: " , consonants)
print("Spaces: " , spaces)
print("Words: " , words)




text = input("Enter a string: ")
reverse = ""

for char in text:
    reverse = char + reverse

print("Reveresd string: " , reverse)



students = ["Ved" , "Ayush", "Hit", "Amit", "Man", "Saqib"]
print("Original list: " , students)

students.append("Kushal")
print("After adding: " , students)

students.remove("Amit")
print("After removing: " , students)

students.sort()
print("Sorted list: " , students)



cities = ("Surat" , "Mumbai" , "ahmedabad" , "Delhi" , "pune")
print("Cities: " , cities)



squares = [num ** 2 for num in range(1 ,21)
           if num % 2 == 0]

print("Squares of even numbres: " , squares)



set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1: " , set1)
print("Set 2: " , set2)


print("Union: " , set1 | set2)
print("Intersection: " , set1 & set2)
print("Difference: " , set1 - set2)


students = {
    "Ayush": {"age": 19, "marks": 85},
    "ved": {"age": 23, "marks": 68},
    "Man": {"age": 22, "marks": 89}
}

for name, details in students.items():
    print("Name: " , name)
    print("Age: " , details["age"])
    print("Marks: " , details["marks"])
    print()


products = [
    {"name": "Laptop" , "price": 55000, "qty": 2},
    {"name": "Mobile" , "price": 55670, "qty": 5},
    {"name": "Tablet" , "price": 12000, "qty": 3},
    {"name": "Headphones" , "price": 3500, "qty": 4},
    {"name": "Moniter" , "price": 56000, "qty": 5}
]
most_expensive = products[0]
for product in products:
    if product["price"] > most_expensive["price"]:
        most_expensive = product


        
print("Most expensive product:")
print("Name: " , most_expensive["name"])
print("Price: " , most_expensive["price"])
print("Quantity: " , most_expensive["qty"])
















      


             
