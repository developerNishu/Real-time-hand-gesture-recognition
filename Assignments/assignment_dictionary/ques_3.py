# Python script to sort (ascending and descending) a dictionary by value.

user_d = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}

l = list(user_d.items())  # convet the given dict. into list

l.sort()  # sort the list
print('Ascending order is', l)  # this print the sorted list

l = list(user_d.items())
l.sort(reverse = True)  # sort in reverse order
print("Descending order is:>", l)

dict = dict(l)  # convert the list in dictionary

print("Dictionary", dict)