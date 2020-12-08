# *Define some collection of names and get the collection of their first 3 characters using map(), print the result
names = ['Toma', 'Anyuta', 'Lrisa', 'Eleonora', 'Anna']
first_3_char = list(map(lambda name: name[:3], names))
print('First 3 characters of our names:', first_3_char)