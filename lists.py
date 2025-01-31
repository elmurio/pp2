#List items are ordered, changeable, and allow duplicate values

thislist = ["apple", "banana", "cherry"]
print(thislist)

#create a list

list = ["apple", "banana", "cherry"]
print(list[1])

#print the second item of the list

thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[2:5])

#return the third, fourth, and fifth item

thislist3 = ["apple", "banana", "cherry"]
thislist3[1] = "blackcurrant"

#change the second item

thislist4 = ["apple", "banana", "cherry"]
thislist4.append("orange")

#append an item

thislist5 = ["apple", "banana", "cherry"]
thislist5.insert(1, "orange")

#insert an item

thislist6 = ["apple", "banana", "cherry"]
thislist6.remove("banana")

#remove item

thislist7 = ["apple", "banana", "cherry"]
for x in thislist7:
    print(x)

#print all items in the list one by one