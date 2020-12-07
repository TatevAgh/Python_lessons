# *Create a function with 2 parameters (function, number),
# call the function with some specific function described with lambda and integer inputed from console

num = int(input('write num : '))
def someFunction(func, num):
    print(func(num))

someFunction(lambda num: num * 2, num)

def plus3(num):
    return num + 3

someFunction(plus3, num)