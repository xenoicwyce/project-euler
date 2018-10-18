from math import sqrt

def fibo(n):
    # Hack: reduce computation time (taken from wolfram)
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

# initialize
sum_ = 0
n = 0
while True:
	fn = fibo(n)
	if fn > 4e6:
        break
    if fn % 2 == 0:
        sum_ += fn
     n += 1

print(sum_)
