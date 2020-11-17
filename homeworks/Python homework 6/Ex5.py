# *Input a collection of employee names with their salary, calculate average salary in organisation,
# get the employee with highest salary, get the employee with lowest salary print results.
employee = {'Anny': 60000, 'Avo': 50000, 'Vars': 25000, 'Sed': 100000}
limit = int(input('Input a limit count for employee`s length: '))
salary = []
average = 0
highest = 0
while len(employee) < limit:
    employee[input('Add a name of employee: ')] = int(input('Add a salary: '))
    limit -= 1

for sal in employee.values():
    salary.append(sal)
    salary.sort()
    
average = sum(salary)//len(salary)
print('Average salary in organisation is:', average)
print('the employee with highest salary is:', salary[-1])
print('the employee with lowest salary is:', salary[0])