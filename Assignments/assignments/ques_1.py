#python program for Find those numbers which are divisible by 7 and multiple of 5,
#between 1500 and 2700 (both Inc)

lower_range = 1500
upper_range = 2700

for i in range(lower_range,upper_range +1):
    if (i % 7 == 0 and i % 5 == 0):
        print(i)
