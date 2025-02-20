import math

def degree_to_radian(d):
    r = d * (math.pi / 180)
    return r

d = int(input("Input degree: "))
r = degree_to_radian(d)
print(f"{d} degree is {r} radian")
