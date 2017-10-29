# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# uncomment to take input from the user
#num = int(input("Enter a number: "))

def fact(n):
	# check if the number is negative, positive or zero
	if num < 0:
	   print("Sorry, factorial does not exist for negative numbers")
	elif num == 0:
	   print("The factorial of 0 is 1")
	else:
	   factorial = 1
	   for i in range(1,num + 1):
	       factorial = factorial*i
	   print("The factorial of",num,"is",factorial)

def fact_recursive(n):
	if n <= 1:
		return 1
	else:
		return n * fact_recursive(n - 1)

fact(num)
print(fact_recursive(num))