# Solution referred from https://stackoverflow.com/questions/45638830/project-euler-23-python-non-abundant-sums """

from functools import reduce
from math import sqrt

def proper_divisors_sum(n):
	""" Return the sum of proper divisors given a number n. """
	if n == 1:
		return 1
	else:
		step = 2 if n%2 else 1
		divs = set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))
		divs.remove(n)
		return sum(divs)

abundant_nums = []
for i in range(1, 28124):
	if i < proper_divisors_sum(i):
		abundant_nums.append(i)

sums = [0] * 28124
for i in range(len(abundant_nums)):
	for j in range(i, len(abundant_nums)):
		sum_of_two = abundant_nums[i] + abundant_nums[j]
		if sum_of_two <= 28123:
			if sums[sum_of_two] == 0:
				sums[sum_of_two] = sum_of_two
				
total = 0
for i in range(1, len(sums)):
	if sums[i] == 0:
		total += i
		
print(total)