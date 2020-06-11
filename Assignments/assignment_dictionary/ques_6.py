# Python script to generate and print a dictionary that contains a number (between 1 and n) in
# the form (x, x*x).

user_input = int(input("Input a number :>"))
my_dict = dict()

for x in range(1,user_input+1):
    my_dict[x]=x*x

print(my_dict)