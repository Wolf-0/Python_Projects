# This program will calculate the sum of all the even numbers upto the given number

a = int(input ("Enter a number "))
result = 0
count = 0
while count <= a:
	if count % 2 == 0:
		result = result + count
		count = count + 1
	else:
		count = count + 1
print ("Sum of even numbers upto %d is %d" %(a,result))