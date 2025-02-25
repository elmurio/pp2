#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

text = input()
matches = re.findall("ab*|a", text)

print(matches)


#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

text = input()
matches = re.findall("ab{2,3}", text)

print(matches)

