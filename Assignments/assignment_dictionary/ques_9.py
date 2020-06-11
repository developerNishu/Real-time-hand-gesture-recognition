# Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.


import itertools      
# d ={'1':['a','b'], '2':['c','d']}
sample_data = {'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[sample_data[k] for k in sorted(sample_data.keys())]):
    print(''.join(combo))