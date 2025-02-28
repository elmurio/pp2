import os

file_path = input()

if os.path.exists(file_path):
    file = open(file_path, 'r')

    count = 0
    for line in file:
        count += 1
    
    print(f"The number of lines in the file is: {count}")
else:
    print(f"The file '{file_path}' does not exist.")


