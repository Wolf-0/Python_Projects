#!/usr/bin/env python3

"""
This program is the implementation of the famous fizzbuzz program.
If the number is divisible by both 3 and 5, then the progrma prints 'FizzBuzz'.
If the enumber is only divisible by 3, then the program prints 'Fizz'
If the enumber is only divisible by 5, then the program prints 'Buzz'
"""
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
        

def fizz_buzz_2(num):
    output = ''
    if num % 3 == 0:
    	output += "Fizz"
    if num % 5 == 0:
    	output += "Buzz"
    if(num % 3 != 0 and num % 5 != 0):
    	output = num
    print(output)

def fizz_buzz_3(num):
    output = ''
    Fizz_Num = 3
    Buzz_Num = 5
    if num % Fizz_Num == 0:
    	output += "Fizz"
    if num % Buzz_Num == 0:
    	output += "Buzz"
    if(num % Fizz_Num != 0 and num % Buzz_Num != 0):
    	output = num
    print(output)


def fizz_buzz4(num,Fizz_Num=3,Buzz_Num=5):
    output = ''
    if num % Fizz_Num == 0:
    	output += "Fizz"
    if num % Buzz_Num == 0:
    	output += "Buzz"
    if(num % Fizz_Num != 0 and num % Buzz_Num != 0):
    	output = num
    print(output)

def fizz_buzz_5(num,Fizz_Num=3,Buzz_Num=5):

    def mod(divident,divisor):
        return (divident % divisor == 0)
    output = ''

    if mod(num,Fizz_Num):
        output += 'Fizz'

    if mod(num,Buzz_Num):
    	output += 'Buzz'

    if (not mod(num,Fizz_Num) and not mod(num,Buzz_Num)):
    	output = num

    print(output)


    
for i in range(1, 101):
    fizz_buzz(i)

