from math import floor

def zeller(day, month, year):
	""" Zeller's congruence:
	h = (q + floor(13*(m+1)/5) + K + floor(K/4) + floor(J/4) + 5*J) % 7
	
	where
		h is the day of the week (0 = Saturday, 1 = Sunday, ... , 6 = Friday)
		q is the day of the month
		m is the month (3 = March, 4 = April, ... , 14 = February)
		K is the year of the century (year % 100)
		J is the zero-based century, i.e. floor(year/100) """
	
	q = day
	if month == 1 or month == 2:
		m = month + 12
		year = year - 1
	else:
		m = month
	K = year % 100
	J = floor(year / 100)
	
	h = (q + floor(13*(m+1)/5) + K + floor(K/4) + floor(J/4) + 5*J) % 7
	return h

num_sunday = 0
for year in range(1901, 2001):
	for month in range(1, 13):
		h = zeller(1, month, year)
		if h == 1:
			num_sunday += 1
			
print(num_sunday)