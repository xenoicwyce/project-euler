import numpy as np

def split_int(n):
	return [int(d) for d in str(n)]
	
li = []
for i in range(4150, int(1e6)): # 4150 is found by previous program run, assume upper limit of 1 million
	if i == np.sum(np.power(split_int(i), 5)):
		li.append(i)
		
print(sum(li))