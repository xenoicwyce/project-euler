def is_palindrome(n):
    s = str(n)
    if s == s[::-1]:
		return True
    else:
        return False
 
palindromes = []
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if is_palindrome(i*j):
            palindromes.append(i*j)

print(max(palindromes))
