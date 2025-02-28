import os

path = input()

if os.path.exists(path):
    print(f"The path '{path}' exists.")
    
    directory = os.path.dirname(path)
    print(f"The directory portion of the path is: '{directory}'")
    
    filename = os.path.basename(path)
    print(f"The filename portion of the path is: '{filename}'")
else:
    print(f"The path '{path}' does not exist.")
