# program to create the multiplication table
# from (1 to 10) of number.

# taking input
number = int(input("Please enter a number between 1-10 :> "))

#checking condition
if(number >= 1 and number <=10):

    for i in range(1,11):
        print(number, "x", i, "=",  number*i)
else:
    print("oops! invailid input")