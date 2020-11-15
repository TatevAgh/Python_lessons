# *Define a collection of numbers, generate a new collection selecting only odd or dividable by 6 numbers and print it

numbers = [12, 7, 45, 6, 79, 36, 77, 18]
index = 1
new_numbers = []

for num in numbers:
    if num%6 == 0 or (index != num/2 and num % index != 0):
        index += 1
        new_numbers.append(num)
print(new_numbers)