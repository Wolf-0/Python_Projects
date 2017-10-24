#!/usr/bin/env python3


def fizz_buzz(num):
    print(num)
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print("Number is not divisible by 3 or 5 or 15")

for i in range(1, 101):
    fizz_buzz(i)

