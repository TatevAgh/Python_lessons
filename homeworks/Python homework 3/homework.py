# Tasks related to part 4:
# *Define a collection of weekdays, print following: first 5 week days, total days number, last 2 days, odd days
# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# print('first 5 week days: ', weekdays[:5])
# print('total days number is: ', len(weekdays))
# print('last 2 days', weekdays[-2:])
# print('odd days', weekdays[::2])

# *Define a collection of colors, add a color from console, print total colors number, print colors on even positions
# colors = ['blue', 'green', 'red','yellow']
# add_color = input('Add a color: ')
# colors.append(add_color)
# print('total colors number: ', len(colors))
# print('colors on even positions: ', colors[1::2])

# *Define collection of numbers, get number at random position if it doesn’t exceed some inputed threshold value
# from random import randint
# numbers = [1, 4, 9, 77, 4, 65, 23]
# value = int(input('input an value: '))
# random_index = randint(0, len(numbers))
# if numbers[random_index] < value:
#     print('it doesn’t exceed inputed value')
# else:
#     print('it exceed inputed value')


# *Define collection of students (names) from group
# 1 and collection of students from group 2, print the collection of students from both groups
# first_group = ['Sevak', 'Hrayr', 'Tigran', 'Tatevik']
# second_group = ['Grigor', 'Levon', 'Arina', 'Robert']
# print('the collection of students from both groups', first_group + second_group)


# *Define a garage collection that stores 3 cars (models), it’s known that double of same models came to garage, print garage models
# models = ['bmw', 'audi', 'bmw']
#
# same_models = []
# for model in models:
#     for same in models:
#         if model == same:
#             same_models.append(same)
#
# print(same_models)
"""sa chhaskaca inchpes anem"""

# *Define a collection of programming languages (names), add new language name from console if it’s not C#
# languages = ['Python', 'Javascript', 'Java', 'C#', 'C++']
# new_language = str(input('Add new language: '))
#
# if new_language != 'C#':
#     languages.append(new_language)
#     print(languages)

# *Define an empty collection, input 3 numbers and add them to collection, calculate factorial for the last one
numbers = []
first_num = int(input('Input First Value: '))
numbers.append(first_num)
sec_num = int(input('Input Second Value: '))
numbers.append(sec_num)
third_num = int(input('Input Third Value: '))
numbers.append(third_num)
last_value = numbers[-1]
print(last_value)
factorial = 1
# if last_value < 0:
#     print('Sorry, factorial does not exist for negative numbers')
# elif last_value == 0:
#     factorial = 1
#     print('Factorial of 0 is ' + factorial)
# else:
print(range(1, last_value + 1))

    # for i in range(1, last_value + 1):
    #     factorial = factorial * i
    # print("The factorial of", last_value, "is", factorial)
    #



# *Define a collection of words, input 2 new words and add them to list, find some inputed word in list and remove a word with some inputed index
# *Define a game board (2x2 matrix) with 2 bomb values and 2 gold values, provide user 3 attempts to find all gold values