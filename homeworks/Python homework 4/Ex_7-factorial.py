# *Define an empty collection, input 3 numbers and add them to collection, calculate factorial for the last one

numbers = []
while len(numbers) != 3:
    numbers.append(int(input('add a number : ')))
print(numbers)
last_num = numbers[-1]
fact_step = 1
factorial = 1
while fact_step <= last_num:
    factorial = factorial * fact_step
    fact_step += 1
print(factorial)