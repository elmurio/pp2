import math

def polygon_area(n, l):
    area = (n * l**2) / (4 * math.tan(math.pi / n))
    return area

n = int(input("Input number of sides: "))
l = float(input("Input the length of a side: "))

area = polygon_area(n, l)
print(f"The area of the polygon is: {area:.2f}")
