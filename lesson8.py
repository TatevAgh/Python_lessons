# arr = [1, 5, 2, 3, 5, 44, 14, 21]
# arr2 = [num for num in arr if num % 2 == 1]
# # nayev karelie ogtagorcel filter()

# arr = [1, 5, 2, 3]
# def multiply_by_3(number):
#     return number * 3
#
# result = list(map(multiply_by_3, arr))
# print(list(map(lambda num: num * 2, arr)))
# print(result)


# words_1 = ['first', 'sec', 'third']
# words_2 = ['six', 'four', 'fifth']
#
# def concat_words(word1, word2):
#     return word1 + word2
#
# result = list(map(concat_words, words_1, words_2))
# print(result)
# print(list(map(lambda word1, word2: word1 + '___' + word2, words_1, words_2)))

# numbers = [2, 5, 11, 8]
# sec = list(filter(lambda x: 3 < x < 10, numbers))
# print((list(filter(lambda num: num < 5, numbers))))
# print(sec)
#
# def is_between_3_10(x):
#     return 3 < x < 10
#
#
# def is_between_3_10(x):
#     if 3 < x < 10:
#         return True
#     else:
#         return False

# numbers = [2, 5, 11, 8]
#
# employees = [{'name': 'Aaron', 'salary': 500}, {'name': 'Mery', 'salary': 600}]
# print(list(map(lambda x : x['name'], employees)))
# map(lambda x : x['salary']*2, employees) # [1000, 1200]
# map(lambda x : x['salary'] < 550, employees) # Output: [True, False]
#
# list_a = [1, 2, 3]
# list_b = [10, 20, 30]
# ggg = list(map(lambda x, y: x + y, list_a, list_b))
# print(ggg)


# words_1 = ['heey', 'yesss', 'ahhhh']
# words_2 = ['youuu', 'nooo', 'ohhh']
#
# words =  list(map(lambda first, second: first + ' ' + second, words_1, words_2))
# print(words)
#
# numbers = [ 5, 8, 7, 66]
# even = list(filter(lambda i: i % 2 == 0, numbers))
# print(even)

# Problem: Create a collection of several employees with some information about them,
# get the employees with information if their position title starts with some symbol, print result

employees = [{'name': 'Gexam', 'position': 'manager', 'stars': 5}, {'name': 'Armen', 'position': 'smm', 'stars': 2}]
employees_w_s = list(filter(lambda x: x['name'][0] == 'G', employees))
print(employees_w_s)

import functools
numbers = [ 5, 8, 7, 66]
print(functools.reduce(lambda x, y: x+y, numbers))
