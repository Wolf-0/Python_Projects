# This program will calculate the investment over a period of time
amount = int (input("Enter the initial amount: "))
inrate = float (input("Enter the interest rate: "))
period = int (input("Enter the time period: "))
val = 0
year = 1
while year <= period:
	value = amount + (inrate*amount)
	print("Year %d Rs. %.2f" % (year, value))
	amount = value
	year = year + 1
