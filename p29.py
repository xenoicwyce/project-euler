li = []
for a in range(2, 101):
	for b in range(2, 101):
		c = a**b
		if c not in li:
			li.append(c)
			
print(len(li))