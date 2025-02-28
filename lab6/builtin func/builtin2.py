input = input("Enter a string: ")

upper = sum(1 for char in input if char.isupper())
lower = sum(1 for char in input if char.islower())

print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")
