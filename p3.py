from math import sqrt
from functools import reduce
from itertools import count, islice

def factors(n):
	""" Return a set of factors given a number n. """
	step = 2 if n%2 else 1
	return set(reduce(list.__add__,
		([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

def is_prime(n):
	""" Determine whether a number n is prime. """
	return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

if __name__ == '__main__':
	n = 600851475143
	for i in reversed(sorted(list(factors(n)))):
		if is_prime(i):
			print(i)
			break