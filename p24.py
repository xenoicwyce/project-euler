from itertools import permutations, islice

k = 1000000
p_gen = permutations(range(10))
print(next(islice(p_gen, k-1, k)))