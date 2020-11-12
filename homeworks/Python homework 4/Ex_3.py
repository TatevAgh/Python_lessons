# *Define collection of numbers, get number at random position if it doesn’t exceed some inputed threshold value

from random import randint
numbers = [1, 4, 9, 77, 4, 65, 23]
value = int(input('input an value: '))
random_index = randint(0, len(numbers))
if numbers[random_index] < value:
    print('it doesn’t exceed inputed value')
else:
    print('it exceed inputed value')