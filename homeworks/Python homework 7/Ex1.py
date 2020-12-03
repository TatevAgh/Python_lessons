# *Input 3 collections of numbers, calculate how many numbers are greater than 10 for first,
# how many numbers are greater than 20 for second and how many numbers are greater than 30 for third collection
# (implement version without functions and version with functions)

num_collection_1 = [10, 50, 8, 44, 45, 6, 12, 36, 5, 40]
num_collection_2 = [8, 36, 5, 40, 25, 4, 2, 3, 4, 20]
num_collection_3 = [2, 14, 3, 4, 20, 15, 88, 44, 45, 6, 12]
count_10 = 0
count_20 = 0
count_30 = 0

for num in num_collection_1:
    if num > 10:
        count_10 += 1

for num in num_collection_2:
    if num > 20:
        count_20 += 1

for num in num_collection_3:
    if num > 30:
        count_30 += 1

print(count_10, 'numbers are greater than 10 for first')
print(count_20, 'numbers are greater than 20 for second')
print(count_30, 'numbers are greater than 30 for third')


def calculating_greater(list, number):
    """"calculates how many numbers from collection are greater than given number"""
    count = 0
    for num in list:
        if num > number:
            count += 1
    print(count, 'numbers are greater than', number)


calculating_greater(num_collection_1, 10)
calculating_greater(num_collection_2, 20)
calculating_greater(num_collection_3, 30)