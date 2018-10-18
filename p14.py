def collatz_steps(n):
	""" Compute the number of steps taken for a number n 
		to be reduced to 1 by Collatz conjecture. """
	step = 0
	while True:
		if n == 1:
			return step
		elif n % 2 == 0:
			n /= 2
			step += 1
		else:
			n = 3*n + 1
			step += 1

num_steps = [1] # 1 step for zero

for i in range(1, 1000001):
	num_steps.append(collatz_steps(i))
	
print('Maximum steps: ', max(num_steps))
print('Number that produced this chain: ', num_steps.index(max(num_steps)))