from functools import reduce
from math import sqrt

def proper_divisors_sum(n):
	""" Return the sum of proper divisors given a number n. """
	step = 2 if n%2 else 1
	divs = set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))
	divs.remove(n)
	return sum(divs)
	
amicable_sum = 0
for i in range(2, 10001):
	a = proper_divisors_sum(i)
	if a == i:
		continue
	b = proper_divisors_sum(a)
	if b == i:
		amicable_sum += a + b
		print((a, b))
		
print(amicable_sum / 2) # divide by 2 because of repeated pairs