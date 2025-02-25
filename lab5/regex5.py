#Write a Python program to insert spaces between words starting with capital letters.

import re

text = input()
matches = ' '.join(re.findall('[A-Z][^A-Z]*', text))

print(matches)

#Write a Python program to convert a given camel case string to snake case.

import re

camel = input()
snake = re.sub('([a-z0-9])([A-Z])', r'\1_\2', camel).lower()
print(snake)