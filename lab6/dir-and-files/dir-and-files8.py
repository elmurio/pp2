import os

path = input()

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print(f"The file '{path}' has been deleted.")
    else:
        print(f"You don't have permission to delete the file '{path}'.")
else:
    print(f"The file '{path}' does not exist.")
