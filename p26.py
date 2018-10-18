""" 
Solved with the help of http://mathworld.wolfram.com/DecimalExpansion.html
Again I have totally amazed and fascinated by the human mathematics, and the intelligence of those who created it.
"""

from math import log

def recurring_length(n):
	""" Return the number of recurring decimals of 1/n. """
	# if n can be expressed in the form of 2^a * 5^b, 
	# then it should not produce any recurring decimal.
	if log(n, 2).is_integer() or log(n, 5).is_integer():
		return 0
	
	periodic_list = [1]
	p = 1
	while True:
		res = 10**p % n
		if res in periodic_list:
			s = periodic_list.index(res)
			t = p - s
			return t
		periodic_list.append(res)
		p += 1

max_length = 0
for i in range(2, 1000):
	r = recurring_length(i)
	if r > max_length:
		max_length = r
		d = i
		
print(d)