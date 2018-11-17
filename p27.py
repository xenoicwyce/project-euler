from math import sqrt
from itertools import islice, count

def is_prime(n):
	""" Determine whether a number n is prime. """
	return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
	
# n = 0: b must be prime
primes = [] # collection of primes under 1000
for i in range(2, 1000):
	if is_prime(i):
		primes.append(i)
		
a_max, b_max, c_max = 0, 0, 0
for a in range(-1000, 1001):
	for b in primes:
		# b > -(40^2 + 40a) and b > max number of primes
		if b <= -1600 - 40*a or b <= c_max:
			continue
		
		c, n = 0, 0
		while is_prime(n**2 + a*n + b):
			c += 1
			n += 1
			
		if c > c_max:
			a_max, b_max, c_max = a, b, c
			
print(a_max * b_max, c_max)