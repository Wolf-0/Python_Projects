# This program will check if a number is prime or not
a = input("Enter a number ")
count = 2
flag = 1
if a == 1:
	print ("Neither prime nor composite")
elif a == 2:
	print ("Prime number")
while count < a:
	if (a % count == 0):
		flag = 0
		break
	count = count + 1
if flag:
	print ("Prime Number")
else:
	print ("Composite Number")