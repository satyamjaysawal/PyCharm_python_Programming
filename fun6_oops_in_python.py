'''
Python is an object-oriented programming language, which means it supports the concepts of classes and objects. Here are some of the key features of Python's object-oriented programming:

Class: A class is a blueprint for creating objects. It defines the properties and methods of an object.

Object: An object is an instance of a class. It has its own state and behavior.

Encapsulation: Encapsulation is the process of hiding the implementation details of an object from the outside world. It is achieved by using access modifiers such as public, private, and protected.

Inheritance: Inheritance is the process of creating a new class from an existing class. The new class inherits the properties and methods of the existing class.

Polymorphism: Polymorphism is the ability of an object to take on many forms. It allows objects of different classes to be treated as if they were the same type of object.

'''


# Here's an example of how to create a class in Python:



class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("The car has started.")

    def stop(self):
        print("The car has stopped.")

my_car = Car("Toyota", "Corolla", 2021)
my_car.start()
my_car.stop()

# 1.Classes and Objects:
# A class is a blueprint for creating objects. Objects are instances of a class. Here's an example:

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

my_dog = Dog("Rufus", "Poodle")
print(my_dog.name) # Output: Rufus

# 2.Encapsulation:
# Encapsulation is the process of hiding the implementation details of an object from the outside world. It is achieved by using access modifiers such as public, private, and protected. Here's an example:

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number # private variable
        self.balance = balance # public variable

my_account = BankAccount("1234", 5000)
print(my_account.balance) # Output: 5000
# print(my_account.__account_number)

# Error: 'BankAccount' object has no attribute '__account_number'

# 3.Inheritance:
# Inheritance is the process of creating a new class from an existing class. The new class inherits the properties and methods of the existing class. Here's an example:

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Dog(Animal):
    def speak(self):
        print("Woof")

my_cat = Cat("Fluffy")
my_dog = Dog("Rufus")

my_cat.speak() # Output: Meow
my_dog.speak() # Output: Woof

# 4.Polymorphism:
# Polymorphism is the ability of an object to take on many forms. It allows objects of different classes to be treated as if they were the same type of object. Here's an example:

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(4, 5), Circle(7)]

for shape in shapes:
    print(shape.area())


# 5.Abstraction:
# Abstraction is the process of hiding unnecessary implementation details from the user. It is achieved by using abstract classes and interfaces. Here's an example:

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
