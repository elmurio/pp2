import os

path = input()

if os.path.exists(path):
    print(f"The path '{path}' exists.")
    
    if os.path.isfile(path):
        print(f"The path '{path}' is a file.")
    elif os.path.isdir(path):
        print(f"The path '{path}' is a directory.")
    
    if os.access(path, os.R_OK):
        print(f"The path '{path}' is readable.")
    else:
        print(f"The path '{path}' is not readable.")
    
    if os.access(path, os.W_OK):
        print(f"The path '{path}' is writable.")
    else:
        print(f"The path '{path}' is not writable.")
    
    # Check if the path is executable
    if os.access(path, os.X_OK):
        print(f"The path '{path}' is executable.")
    else:
        print(f"The path '{path}' is not executable.")
else:
    print(f"The path '{path}' does not exist.")
