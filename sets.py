#Set items are unordered, unchangeable, and do not allow duplicate values

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#True and 1 is considered the same value

thisset1 = {"apple", "banana", "cherry"}
print("banana" in thisset1)

#Check if "banana" is present in the set

#The union() and update() methods joins all items from both sets.
#The intersection() method keeps ONLY the duplicates.
#The difference() method keeps the items from the first set that are not in the other set(s).
#The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#Join set1 and set2 into a new set
#You can use the | operator instead of the union() method, and you will get the same result.