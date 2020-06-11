# program to sum of two given integers. However, if the sum is between 15 to 20
# it will return 20

# taking input
valueOne = int(input("Enter first value :> "))
valueTwo = int(input("Enter second value :> "))
# addition
sum = valueOne + valueTwo
# checking condition
if(sum > 15 and sum < 20):
    print("20")
else:
    print("oops! enter appropriate values")