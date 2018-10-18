from itertools import count, islice
from math import sqrt

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

i = 2
n = 1
while True:
    if is_prime(i):
        n += 1
        if n == 10002:
            print(i)
            break

    i += 1