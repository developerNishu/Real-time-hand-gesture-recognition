# Python program to create a dictionary from a strin
# Note: Track the count of the letters from the string.

from collections import defaultdict, Counter
str1 = 'RapidCode Technologies' 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print("string is :> ", str1 , end = "\n\n")
print(my_dict)