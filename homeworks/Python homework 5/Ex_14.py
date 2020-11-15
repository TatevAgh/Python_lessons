# *Define a collection of pets, that stores types of pet and its name,
# find how many pets have name Johny and print the number

pets = {'dog': 'Jenny', 'cat': 'Cat ', 'cat': 'Johny', 'bird': 'Any', 'rabbit': 'Johny'}
count = 0
for name in pets.values():
    if name == 'Johny':
        count += 1
print('Count of names `Johny` is: ', count)