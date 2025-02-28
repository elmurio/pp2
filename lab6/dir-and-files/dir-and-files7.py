source_file = input()
destination_file = input()

with open(source_file, 'r') as src:
    content = src.read()

with open(destination_file, 'w') as dest:
    dest.write(content)

print(f"The contents of '{source_file}' have been copied to '{destination_file}'")
