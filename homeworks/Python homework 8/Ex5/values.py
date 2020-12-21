import random

limit = int(input('Write a length of our collections: '))

list_1 = []
list_2 = []

for i in range(0,limit):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    list_1.append(num1)
    list_2.append(num2)

randomlist_1 = tuple(list_1)
randomlist_2 = tuple(list_2)

def words_generator():
    words = []
    while len(words) < limit:
        words.append(input('Write Names: '))
    return words

words_collection1 = words_generator()
words_collection2 = words_generator()

