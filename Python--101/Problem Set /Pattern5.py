n = input ("Enter a number: ")
k = 2*n + 2
z = 0
for i in range (1 , n + 2, +1):
	k = k - 2
	print (" " * k),
	for j in range (1, i , +1):
		print (j),
	for m in range (i-2, 0, -1):
			print (m),
	print ("")
for l in range (n + 2, 1, -1):
	z = z + 2
	print (" " * z),
	for o in range (1 , l-3, +1):
		print(o),
	for n in range (l-3, 0, -1):
		print (n),
	print("")