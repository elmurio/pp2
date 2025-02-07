class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#Use the words mysillyobject and abc instead of self
#The self parameter is a reference to the current instance of the class,
#and is used to access variables that belong to the class

class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p2 = Person1("John", 36)

p2.age = 40

print(p2.age)

#You can modify properties on objects like this, and also delete them using "del"

#class definitions cannot be empty, but if you for some reason have a class definition
#with no content, put in the pass statement to avoid getting an error.