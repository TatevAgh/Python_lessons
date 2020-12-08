# *Calculate subtraction of numbers collection using reduce.
import functools
numbers = [2, 68, 4, 15, 7]
subtraction = functools.reduce(lambda a, b: a + b, numbers)
print('subtraction of numbers collection is:', subtraction)