import functools
import values

def dividable_by(list):
    """"Calculates how many numbers dividable by 6"""
    new_list = []
    number = int(input('input dividable number: '))
    for num in list:
        if num %number == 0:
            new_list.append(num)
    return new_list

def square_sum(n):
    square_sum = 0
    for i in n:
        square_sum = square_sum + (i * i)
    return square_sum

def count_even_numbers(numbers):
    count = 0
    for num in numbers:
        if num %2 == 0:
            count += 1
    return count

# subtraction = functools.reduce(lambda a, b: a + b, values.randomlist_1, values.randomlist_2)