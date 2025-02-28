import os

path = input()

directories = []
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path, item)):
        directories.append(item)

print("Directories:")
print(directories)

files = []
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        files.append(item)

print("\nFiles:")
print(files)

all_items = os.listdir(path)
print("\nAll items (files and directories):")
print(all_items)

