#A lambda function is a small anonymous function.

x = lambda a, b : a * b
print(x(5, 6))

#Multiply argument a with argument b and return the result

def myfunc(n):
  return lambda i : i * n

mydoubler = myfunc(2)

print(mydoubler(11))

#Use that function to make a function that always doubles the number you send in

