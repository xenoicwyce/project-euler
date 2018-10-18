import numpy as np

with open('p13_digits.txt') as f:
	fifty_nums = f.read()
	
int_arr = np.array([int(k) for k in fifty_nums.split('\n')])
first_ten_digits = str(np.sum(int_arr))[:10]

print(first_ten_digits)