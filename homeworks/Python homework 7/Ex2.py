# *Input a collection of numbers, calculate how many numbers are positive and dividable by 6
# (create a function), generate a new collection of odd numbers (create a function), print results

num_collection = [2, 14, 3, 4, -20, 15, 88, 44, 45, 6, 12, -44, 45, 0, 12]

def positive_div_6(list):
    """"Calculates how many  numbers are positive and dividable by 6"""
    for num in list:
        if num > 0 and num %6 == 0:
            print('this is ', num)

positive_div_6(num_collection)

n = []
def odd_number_generator():
    """"Calculates odd numbers"""
    import random
    randomlist = []
    for i in range(0, 20):
        n = random.randint(1, 100)
        if n % 2 == 1:
            randomlist.append(n)
    print('this is list with odd numbers' , randomlist)

odd_number_generator()
