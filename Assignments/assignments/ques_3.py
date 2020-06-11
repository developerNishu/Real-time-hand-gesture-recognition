# program that takes user word and reverse it
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

# def reverse(string):
#     string = string[::-1]
#     return string

string = input("enter the string =>")
print("and the reverse is=>",reverse(string))