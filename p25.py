from math import sqrt, floor

def fibo_iter():
	a, b = 0, 1 # initial values
	while True:
		yield a
		a, b = b, a+b
	
ctr = 0
for f in fibo_iter():
	if len(str(f)) >= 1000:
		print(ctr)
		break
	ctr += 1