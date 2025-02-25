#Write a python program to convert snake case string to camel case string.

import re

snake = input()
words = re.split('_', snake)
camel = words[0] + ''.join(word.capitalize() for word in words[1:])

print(camel)

#Write a Python program to split a string at uppercase letters.

import re

text = input()
matches = re.findall("[A-Z][^A-Z]*", text)

print(matches)