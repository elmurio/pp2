#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

text = input()
matches = re.findall("a.*b", text)
print(matches)

#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

text = input()
matches = re.sub("[ ,.]", ":", text)

print(matches)