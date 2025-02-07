#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

#simpliest example

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p2 = Person("John", 36)

print(p2.name)
print(p2.age)

#built-in __init__() function 
#Create a class named Person, use the __init__() function to assign values for name and age

class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"    

p3 = Person1("John", 36)

print(p3)

#The __str__() function controls what should be returned 
#when the class object is represented as a string

