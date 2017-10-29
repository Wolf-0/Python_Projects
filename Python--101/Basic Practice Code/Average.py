# This program will calculate the average of N numbers
N = 10
sum = 0
count = 0
while count < N:
	number = float (input(""))
	sum = sum + number
	count = count + 1
average = sum / N
print ("Number = %d Sum = %f" % (N,sum))
print ("Average= %f" % (average))