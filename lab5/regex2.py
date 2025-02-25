#Write a Python program to find sequences of lowercase letters joined with a underscore

import re

text = input()
matches = re.findall("[a-z]_[a-z]", text)

print(matches)

#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

text = input()
matches = re.findall("[A-Z][a-z]", text)

print(matches)