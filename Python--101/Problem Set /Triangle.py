# This program will check if the given sides are of an isosceles, scalene or equilateral triangle
a = input ("Enter value of side 1  ")
b = input ("Enter value of side 2  ")
c = input ("Enter value of side 3  ")
if a == b and b == c:
	print("Equilateral Triangle")
elif a == b or b == c or c == a:
	print("Isosceles Triangle")
else:
	print("Scalene Triangle")