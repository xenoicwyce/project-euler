from math import sqrt
from itertools import islice, count

def is_prime(n):
	""" Determine whether a number n is prime. """
	return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
	
ab = []
for a in range(-999, 1000):
	for b in range(-1000, 1001):
		ab.append((a, b))
		
print(ab)