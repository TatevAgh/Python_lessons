# Calculate multiplication of numbers from 0 to inputed value and print it
count = 1
multiplication = 1
value = int(input('Write a number: '))
while value >= count:
    multiplication *= count
    count += 1

print('Value of of numbers from 0 to inputed value:', multiplication)
