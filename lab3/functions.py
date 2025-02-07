#A function is a block of code which only runs when it is called.

def my_function1():
  print("Hello from a function")

my_function1()

#To call a function, use the function name followed by parenthesis

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Information can be passed into functions as arguments

def my_function2(*kids):
  print("The youngest child is " + kids[2])

my_function2("Emil", "Tobias", "Linus")

#If the number of arguments is unknown, add a * before the parameter name

def my_function3(country = "Norway"):
  print("I am from " + country)

my_function3("Sweden")
my_function3("India")
my_function3()
my_function3("Brazil")

#If we call the function without argument, it uses the default value

def my_function4(x):
  return 5 * x

print(my_function4(3))
print(my_function4(5))
print(my_function4(9))

#To let a function return a value, use the return statement

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

#recursion
