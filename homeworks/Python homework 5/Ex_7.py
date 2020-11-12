# *Input string, find how many ‘ab’-s are inside*Input string, find how many ‘ab’-s are inside

str_1 = input('Input string to find ‘ab’-s count: ')
count = 0
index = 0
for i in str_1:
    if str_1[index] == 'a' and str_1[index+1] == 'b':
            count += 1
    index+=1
print('Count of `ab`-s in your inputed word is : ', count)
