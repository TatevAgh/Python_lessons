# *Calculate number of ‘d’ chars in inputed string
str_1 = input('Write some word to calc \'d\' chars: ')
len_str = len(str_1)
count = 0
for i in range(0, len(str_1)):
    if str_1[i] == 'd':
        count += 1
print('Number of ‘d’ chars in inputed string is : ', count)