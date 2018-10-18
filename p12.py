from math import sqrt
from functools import reduce
import numpy as np

def factors(n):
	""" Return a set of factors given a number n. """
    step = 2 if n%2 else 1
    return set(reduce(list.__add__,
		([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))
		
def triangle_num(n):
	""" Return the triangle number of the number n. """
	return np.sum(np.arange(n, dtype='int'))
	
n = 7
while True:
	n_factors = len(factors(triangle_num(n)))
	if n_factors > 500:
		print(triangle_num(n))
		break
	n += 1