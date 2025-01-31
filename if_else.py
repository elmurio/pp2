a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#In this example a is greater than b, so the first condition is not true, 
#also the elif condition is not true, so we go to the else condition 
#and print to screen that "a is greater than b"

c = 330
d = 330
print("A") if a > b else print("=") if a == b else print("B")

#One line if else statement, with 3 conditions  