#Inheritance allows us to define a class that inherits all the methods and properties from another class.

#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#parent class

class Student(Person):
  pass

#child class

class Student(Person):
  def __init__(self, fname, lname):
    #add properties

#When you add the __init__() function, 
#the child class will no longer inherit the parent's __init__() function.

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

#Python also has a super() function that will make the child class inherit 
#all the methods and properties from its parent

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

#Add a property called graduationyear to the Student class

