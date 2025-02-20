def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())

decr = countdown(n)

for i in decr:
    print(i)