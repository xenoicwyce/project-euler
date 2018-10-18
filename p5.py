def is_divisible_until_20(n):
    for i in range(11, 21):
        if n % i != 0:
            return False

	return True

n = 2520
while True:
    if is_divisible_until_20(n):
        print(n)
        break
    else:
        n += 1