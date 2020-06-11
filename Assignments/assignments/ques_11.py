# program that reades two integers representing a month and day
# and prints the season for that month and day.

month = int(input("Input the month (e.g. 1 for January, 2 for February etc.):> "))
day = int(input("Input the day:> "))

if month in range(1,4):
	season = 'winter'
elif month in range(4,7):
	season = 'spring'
elif month in range(7,10):
	season = 'summer'
else:
	season = 'autumn'

if (month == 3) and (day > 19):
	season = 'spring'
elif (month == 6) and (day > 20):
	season = 'summer'
elif (month == 9) and (day > 21):
	season = 'autumn'
elif (month == 12) and (day > 20):
	season = 'winter'

print("Season is: >",season)