# *Create several functions store them inside variables for handling collection of movie names using lambdas
# *Create a function with 2 parameters (function, number),
# call the function with some specific function described with lambda and integer inputed from console
#functia vore uni vorpes parameter functia ev number,

# stexcel ashxatoxneri anunneri collection, tpel ashxatoxneri anunnery voronq sksvum en m

# workers = ['Mariam', 'liza', 'Mary', 'Gevorg', 'Arina']
# for emp in workers:
#     if emp[0] == 'M':
#         print(emp)

######################
# workers = ['Mariam', 'liza', 'Mary', 'Gevorg hayk', 'Arina']
# workers_g = [name for name in workers if name[0] == 'G']
# workers_ = [name for name in workers if ' ' in name]
# print(workers_g)
# print(workers_)

# workers = ['Mariam', 'liza', 'Mary', 'Gevorg hayk', 'Arina']
# workers_a = list(filter(lambda name: name[0] == 'A', workers)) ## lambda returns true  or false
# print(workers_a)
# add = lambda a, b: a + b
# print(add(5,2))

#stexcel tveri collection, gtnel ayn tveri gumare vronq bajanvum en 3i
# numbers = [1, 88, 45, 23, 14, 21]
# sum = 0
# for num in numbers:
#     if num % 3 == 0:
#         sum += num
#
# print(sum)
# #compiration expression
# numbers_3 = [num for num in numbers if num % 3 == 0]
# # numbers_3 = filter(lambda num: num % 3 == 0, numbers)
# import functools
# result = functools.reduce(lambda a, b: a + b, numbers_3)
# print(result)

# *Create several functions store them inside variables for handling collection of movie names using lambdas
# collection_movies = ['Bacurau', 'THE GENTLEMEN', 'First Cow', 'Collective', 'THE GREEN BOOK', 'Martin Eden', 'Soul', 'THE OTHER LAMB']
# is_the = lambda name: name.lower()[:3] == 'the'
# movies_w_the = list(filter(is_the, collection_movies))
# print(movies_w_the)
#
# num = int(input('write num : '))
# def someFunction(func, num):
#     print(func(num))
#
# someFunction(lambda num: num * 2, num)
#
# def plus3(num):
#     return num + 3
#
# someFunction(plus3, num)


# haytararel usanoxneri anunneri collection , tpel kent indexov anunnere, ev tpel verjin anune
# students = ['Aram', 'Ani', 'Hakop', 'Levon', 'Meri', 'Sevak', 'Hrayr']
# print(students[1::2], students[-1])
# for index in range(0, len(students)):
#     if index % 3 == 0:
#         print(students[index])

#haytararel meqenaneri collection, mutqagrel meqenayi anun ,
# stugel ayd meqenan ka mer collectioni mej ete ayo apa tpel indexe

# cars = ['bmw', 'mers', 'audi', 'lada', 'infiniti', 'volkswagen']
# car_name = input('input car name: ')
# # tarberak 1
# # if car_name in cars:
# #     print(cars.index(car_name))
# #
# #tarberak 2
# for index in range(0, len(cars)):
#     if cars[index] == car_name:
#         print(index)
#

#stexcel guyneri coll 2 hat, tpel guynere aranc krknutyunneri,
#tpel ayn guynere voronq kan arajinum ev chkar 2rdum

# colors_1 = {'sev', 'spitak', 'karmir', 'kanach'}
# colors_2 = {'dexin', 'sev', 'kapuyt', 'kanach'}
# print('aranc krknutyunneri bolor guynere: ', colors_1 | colors_2)
# print('kan arajinum ev chkar 2rdum: ', colors_1 - colors_2 )

#mutqagrel text hashvel qani hat 'ab' ka meje,
# u ardyoq ayd tive zuyg e te che

# text = input('write some text: ')
# count = text.count('ab')
# if count % 2 == 0:
#     print('zuyg')
# else:
#     print('kent')
# # print(help(str.count))
# print(count)

# tveri collection tpel skzbic minchev kese
# num = [10, 5, 98, 4, 6, 44, 2, 4, 22]
# print(num[:len(num) // 2])

# stexcel usanoxneri ebv irenc bajinneri collection,
# hashvel qani hat unikal bajin ka, qani usanox ka, tpel vor bajnum e mutqagrac usanoxy, qani bajinneri anune sksum e s ov
#avelacnel usanox ir bajnov
#
# students = {'Arina': 'tntes', 'Hrayr': 'sport', 'Sevak': 'it', 'Levon': 'tntes', 'Tatev': 'service'}
# unical_bajin = set(students.values())
#
# count_s = 0
# for name in students.keys():
#     if name.lower()[0] == 's':
#         count_s += 1
# # count_s = filter(lambda name: )
#
# # input_student = input('input students name: ')
# # for student in students:
# #     if input_student in student:
# #         print(student, 'studied in', students[student], 'department')
#
# #adding student
# students[input('input a name of student: ')] = input('input a department for student ')
#
# print('unikal bajinneri qanake: ', len(unical_bajin))
# print('usanoxneri qanake: ', len(students))
# print('S tarov sksvox usanoxneri qanake: ', count_s)
# print('all list of students: ', students)
#
#
# import multiprocessing
# print('CPU count:', multiprocessing.cpu_count())
