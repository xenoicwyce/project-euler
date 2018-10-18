def num_to_word(n):
	""" Convert a number n to its word form. Only works until 1000. """
	basis = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
			'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	tens  = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	
	if n == 1000:
		return 'onethousand'
	elif n < 20:
		return basis[n]
	elif n >= 20:
		n_str = str(n)
		if len(n_str) == 2:
			return tens[int(n_str[0])] + basis[int(n_str[1])]
		elif len(n_str) == 3:
			first, second, third = n_str[0], n_str[1], n_str[2]
			tail = int(second+third)
			if tail < 20:
				tail_word = basis[tail]
			else:
				tail_word = tens[int(second)] + basis[int(third)]
			
			if tail_word == '':
				return basis[int(first)] + 'hundred'
			else:
				return basis[int(first)] + 'hundredand' + tail_word
	else:
		return ''
			
s = ''
for i in range(1, 1001):
	s += num_to_word(i)
	
print(len(s))