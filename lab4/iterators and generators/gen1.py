def generate_squares(n):
    for i in range(n + 1):
        yield i ** 2

N = int(input())
squares = generate_squares(N)

for square in squares:
    print(square)
