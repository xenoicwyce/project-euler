for n in range(1, 1000):
	for m in range(n+1, 1000):
		# Euclid's formula
		a = m*m - n*n
		b = 2*m*n
		c = m*m + n*n
		if a + b + c == 1000:
			print((a, b, c))
			print(a * b * c)
			exit
		elif a + b + c > 1000:
			break