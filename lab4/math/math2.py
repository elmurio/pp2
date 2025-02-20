def trapezoid_area(h, a, b):
    area = (a + b) * h / 2
    return area

h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))

area = trapezoid_area(h, a, b)

print(f"The area of trapezoid is: {area}")