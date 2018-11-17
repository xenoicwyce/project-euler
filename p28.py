sum_ = 1 # start with 1 as the initial 1 is not added in the loop
n = 1
current_num = 1

while n <= 500: # max step is 1000
	step = 2*n
	""" 
	The diagonal numbers of one full round is:
		current_num + step
		current_num + 2*step
		current_num + 3*step
		current_num + 4*step
	Thus, their sum is 4*current_num + 10*step
	"""
	sum_ += 4*current_num + 10*step
	n += 1
	current_num += 4*step
	
print(sum_)