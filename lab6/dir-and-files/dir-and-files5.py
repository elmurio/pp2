path = input()
list = input().split(',')

with open(path, 'w') as file:
    for item in list:
        file.write(item.strip() + "\n")

print(f"Список записан в файл '{path}'")
