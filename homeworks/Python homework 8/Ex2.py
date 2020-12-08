# *Input 2 collections of numbers,
# get the collection where each i-th element is square sum of corresponding elements in that 2 collections,
# print result

length = int(input('Input an length of our collections: '))
first_coll = []
second_coll = []
while len(first_coll) < length:
    first_coll.append(int(input('write a number for first collection: ')))
    second_coll.append(int(input('write a number for second collection: ')))

print(first_coll, second_coll)

def square_sum(n):
    square_sum = 0
    for i in n:
        square_sum = square_sum + (i * i)
    return square_sum

print('This is Square sum of first Collection: ', square_sum(first_coll))
print('This is Square sum of second Collection: ', square_sum(second_coll))