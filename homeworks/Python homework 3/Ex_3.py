# *Input 2 numbers from console and check if both of them are positive

value1 = int(input('Please input first value: '))
value2 = int(input('Please input second value: '))

if value1 > 0 and value2 > 0:
    print('both are positive')
else:
    print('one is negative')