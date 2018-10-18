from itertools import count, islice
from math import sqrt

def is_prime(n):
	""" Determine whether a number n is prime. """
	return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))
	
sum_ = 0
for i in range(2, 2000000):
	if is_prime(i):
		sum_ += i
		
print(sum_)