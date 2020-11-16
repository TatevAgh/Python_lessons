# *Create a collection of students with their scores and input them from console,
# remove students with score less than 40 and print final collection
#
students = {}
limit = 0
while limit < 2:
    students[input('Enter Name of Student: ')] = int(input('Add score: '))
    limit += 1

print(students)

students = {key: value for key, value in students.items() if value > 40}
print(students)
