# *Input string of words separated by coma, get number of words and print it
str_1 = input('Input string of words separated by coma: ')
number_of_words = str_1.count(',') + 1
print(number_of_words)

"""or"""
str_1 = input('Input string of words separated by coma: ')
count = 1
for i in range(0, len(str_1)):
    if str_1[i] == ',':
        count += 1
print(count)