# *Create a calculator with different functions:
# 1) input numbers (one or more);
# 2) calculate different power for inputed numbers;
# 3) calculate how many numbers are greater than some specific number;
# 4) calculate how many numbers are even;
# 5) get number which power 3 is greater than 100

amount = int(input('Please Input amount of numbers: '))
numbers = []
while(len(numbers) < amount):
    numbers.append(int(input('Please input a number: ')))

def calc_power(numbers):
    """"calculating different power for inputed numbers,
    and gets number whitch power of 3 is greater than 100"""
    new_numbers = []
    power = int(input('Please write power for calculating numbers: '))
    for num in numbers:
        new_numbers.append(pow(num, power))
        if (power == 3 and pow(num, power)) > 100:
            print(num, '\'s power of 3 is greater than 100')

    return new_numbers

def greater_than(numbers):
    """ calculating how many numbers are greater than some specific number"""
    specific_num = int(input('Input a specific number for calculating: '))
    count = 0
    for num in numbers:
        if num > specific_num:
            count += 1
    return count

def even_numbers(numbers):
    count = 0
    for num in numbers:
        if num %2 == 0:
            count += 1
    return count


print('calculating different power of inputed numbers:', calc_power(numbers))
# print('Count of numbers that are greater than some specific number is:', greater_than(numbers))
print('Count of even numbers is:', even_numbers(numbers))

