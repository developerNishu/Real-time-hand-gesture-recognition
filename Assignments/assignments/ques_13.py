# program to get next day of a given date

# taking yaer
year = int(input("Please enter year :> "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

# taking month
month = int(input("Please enter month [1-12] :> "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30

# taking date
date = int(input("Please enter date :> "))
if date < month_length:
    date += 1
else:
    date = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

# printing next date
print("The next date is [yyyy-mm-dd] :> %d-%d-%d <: " % (year, month, date))