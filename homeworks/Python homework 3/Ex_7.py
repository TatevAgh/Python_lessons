# *Generate a random number from 1 to 100 and check if the number is greater than 15 and less than 36

import random
rand_number = random.randint(1, 100)
if rand_number > 15 and rand_number < 36:
    print('Number is greater than 15 and less than 36, number is: ', rand_number)
else:
    print('Number isn\'t greater than 15 and less than 36, number is: ', rand_number)