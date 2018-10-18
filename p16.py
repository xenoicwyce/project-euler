import numpy as np

s = str(2 ** 1000)
a = np.array([int(k) for k in s])

print(np.sum(a))