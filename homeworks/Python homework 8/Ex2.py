# *Input 2 collections of numbers,
# get the collection where each i-th element is square sum of corresponding elements in that 2 collections,
# print result

length = int(input('Input an length of our collections: '))
first_coll = []
second_coll = []
while len(first_coll) < length:
    first_coll.append(input('write a number for first collection: '))
    second_coll.append(input('write a number for second collection: '))

print(first_coll, second_coll)