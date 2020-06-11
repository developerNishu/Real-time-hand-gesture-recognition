# program to check whether the entered character is vowel or consonant

user_input = input("Enter a character: ")

if(user_input =='A' or user_input =='a' or user_input =='E' or user_input =='e' or user_input =='I'
or user_input =='i' or user_input =='O' or user_input =='o' or user_input =='U' or user_input =='u'):
    print(user_input, "is a Vowel")
else:
    print(user_input, "is a Consonant")