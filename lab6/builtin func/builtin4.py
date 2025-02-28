import time
import math

def calculate_square_root(number):
    return math.sqrt(number)

number = float(input())
delay_ms = int(input())

delay_sec = delay_ms / 1000
time.sleep(delay_sec)

result = calculate_square_root(number)

print(f"The square root of {number} is {result}")
