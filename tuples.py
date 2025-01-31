#Tuple items are ordered, unchangeable, and allow duplicate values

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

#convert the tuple into a list to be able to change it

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

#create a new tuple with the value "orange", and add that tuple

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#join two tuples


