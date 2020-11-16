# *Input a string, print it from start to half if its length is even, otherwise from half to the end
str_1 = input('Input some string: ')
print(str_1[1::2]) if (len(str_1)%2 == 0) else print(str_1[::2])