import string

def alphabet_score(name):
	alphabets = string.ascii_uppercase
	score = 0
	for letter in name:
		score += alphabets.index(letter) + 1
		
	return score
	
with open('p022_names.txt') as f:
	names = f.read()
	
name_list = sorted(names.replace('"', '').split(','))

scores = []
for i, name in enumerate(name_list, 1):
	scores.append(alphabet_score(name) * i)
	
print(sum(scores))