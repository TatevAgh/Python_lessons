import values
import operations

numbers1 = operations.dividable_by(values.randomlist_1)
numbers2 = operations.dividable_by(values.randomlist_2)

print(numbers1)
print(numbers2)

print('First collection of numbers dividable by inputed number: ', numbers1) if len(numbers1) >= 1 else print('Collection is empty')
print('First collection of numbers dividable by inputed number: ', numbers2) if len(numbers1) >= 1 else print('Collection is empty')

print('First 3 characters of first collection Names: ', list(map(lambda name: name[:3], values.words_collection1)))
print('First 3 characters of first collection Names: ', list(map(lambda name: name[:3], values.words_collection2)))

print('Square sum of first collection: ', operations.square_sum(values.randomlist_1))
print('Square sum of second collection: ', operations.square_sum(values.randomlist_2))

print('Count of even numbers in first collection is : ', operations.count_even_numbers(values.randomlist_1))
print('Count of even numbers in second collection is : ', operations.count_even_numbers(values.randomlist_2))