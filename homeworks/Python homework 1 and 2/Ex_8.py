# *Write a program containing 3 modules:
# 1. calculating power of number (number and power are inputed from console),
import module1
print('This is reply from first module; ', module1.reply_1_module)

# 2. calculating remainder of some number devidied to other number (inputed from console),
import module2
print('This is reply from second module; ', module2.reply_2_module)
# 3. performing operation from first and second module

result = module1.reply_1_module - module2.reply_2_module
print(result)