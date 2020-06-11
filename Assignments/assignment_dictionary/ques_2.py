# program to convert given list to list of dictionarie

sample_colours = ['black', 'red', 'maroon', 'yellow']
sample_codes = ['#0007', '#0006', '#0005', '#0004']

# Printing original keys-value lists
print("Original key list is : " + str(sample_colours))
print("Original value list is : " + str(sample_codes))

# using zip()
result = dict(zip(sample_colours, sample_codes))

# Printing  dictionary
print("Resul dictionary is : " + str(result))