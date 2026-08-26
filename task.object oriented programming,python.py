class car:
    def __init__(self , brand , model , year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = car("Toyota" , "Fortuner" , 2023)
car2 = car("Honda" , "Ctiy" , 2022)

print(car1.brand , car1.model , car1.year)
print(car2.brand , car2.model , car2.year)




class BankAccount:
    def __init__(self , name , balance):
        self.name = name
        self.balance = balance
        print("Account created")

    def __del__(self):
        print("Account deleted")

account = BankAccount("Ayush" , 700000)
print("Name: " , account.name)
print("Balance: " , account.balance)






class Student:
    def __init__(self , name , marks):
        self.___name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self , marks):
        self.__marks = marks


student = Student("Ayush" , 90)
print("Marks: " , student.get_marks())

student.set_marks(98)
print("Updated Marks: " , student.get_marks())





class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()





class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof!'")

animal = Animal()
dog = Dog()

animal.speak()
dog.speak()


from abc import ABC , abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self , radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self , length , width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

Circle = Circle(5)
rectangle = Rectangle(10 , 5)

print("Circle Area:" , Circle.area())
print("rectangle Area:" , rectangle.area())






class Animal:
    def __init__(self , name):
        self.name = name
        print("Animal constructor called")
class Dog(Animal):
    def __init__(self , name , breed):
        super().__init__(name)
        self.breed = breed

dog = Dog("Tommy" , "German Shepherd")
print("Name:" , dog.name)
print("Breed:" , dog.breed)



    

        
        

                
