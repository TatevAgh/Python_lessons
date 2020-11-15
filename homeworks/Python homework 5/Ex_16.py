# *Create a collection of students with their scores and input them from console,
# remove students with score less than 40 and print final collection

students = {'Sona': 50, 'Vahan': 45}
print(len(students))
print(students.values())
# while len(students) < 4:
#     add_student = input('Enter Name of Student: ')
#     students[add_student] = int(input('Add score: '))
for student in students:
    print(student)