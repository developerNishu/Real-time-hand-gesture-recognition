# Python program which accepts a sequence of comma separated 4 digit binary numbers
# as its input and print the numbers that are divisible by 5 in a comma separated sequence.

# value = []
# items=[x for x in raw_input().split(',')]
# for p in items:
#     intp = int(p, 2)
#     if not intp%5:
#         value.append(p)
#
# print ','.join(value)

values = input("enter data => ")
split_value = values.split(", ")
print(split_value)
for i in range(split_value):
    if(i % 5 ==0):
        print(i)
    print(" ")