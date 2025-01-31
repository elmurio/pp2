fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#Exit the loop when x is "banana"

for x in range(2, 30, 3):
  print(x)

#Using the range() function

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Break the loop when x is 3, and see what happens with the else block

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#Print each adjective for every fruit