#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

part_1 = f"Last digit of {number} is {last_digit}"

if last_digit > 5:
    print(f"{part_1} and is greater than 5")
elif last_digit == 0:
    print(f"{part_1} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"{part_1} and is less than 6 and not 0")
