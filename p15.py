""" Solution re-implemented from http://code.jasonbhill.com/python/project-euler-problem-15/ (Dynamic Python Solution) """

import numpy as np

def num_routes(lattice_size):
	""" Returns the number of route possible given a lattice size. """
	lattice = np.ones((lattice_size+1, lattice_size+1), dtype='int64')
	for i in range(1, lattice_size+1):
		for j in range(1, lattice_size+1):
			lattice[i, j] = lattice[i-1, j] + lattice[i, j-1]

	return lattice[lattice_size, lattice_size]
	
print(num_routes(20))