# *Create 2 collections storing company employees, get number of employees working in both companies,
# get collection of employees with some name from both of groups,
# input several names and find if they work in one of companies, print results

first_company = ['Anny', 'Avo', 'Vars', 'Sed', 'Sona']
second_company = ['Henry', 'Georgy', 'Anny', 'Toma']
print('Number of employees working in both companies: ', len(first_company) + len(second_company))
some_employees = first_company[2:-1] + second_company[:2]
print('Employees with some name from both of groups:', some_employees)
count = 0
while count < 2:
    name = input('Write a name that can be in our list: ')
    if name in first_company:
        print('this employee is in first company')
    else:
        print('this employee isn`t in first company')
    if name in second_company:
        print('this employee is in second company')
    else:
        print('this employee isn`t in second company')
    count += 1
