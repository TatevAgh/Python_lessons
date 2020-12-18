# *Create a class for representing employee with some attributes
# (name, position, salary, workdays (weekdays), completed tasks names)
# and behavior (change position, check if salary is higher than some threshold,
# find how many days salary works per week, find if employee works on some specific weekday),
# create several employees and perform actions, check how many employees are defined


class Employee:
    counter = 0
    def __init__(self, name, position, salary, workdays, tasks):
        self.name = name
        self.position = position
        self.salary = salary
        self.workdays = workdays
        self.tasks = tasks
        self.done_tasks = []

        Employee.counter += 1

    def change_position(self, new_position):
        self.position = new_position
        return self.position

    def is_higher(self, threshold):
        if self.salary >= threshold:
            print(self.name, 'employee\'s salary is higher than', threshold)
        else:
            print(self.name, 'employee\'s salary is lower than', threshold)

    def salary_per_day(self):
        money = self.salary // (4 * len(self.workdays))
        return money

    def check_workdays(self, workday):
        if workday in self.workdays:
            print(workday, 'exist in ', self.name, '\'s workdays')
        else:
            print('weekday doesn\'t ', self.name, '\'s workdays')

    def finished_tasks(self):
        for task in self.tasks.items():
            if task[1] == 'Done':
                self.done_tasks.append(task[0])
        print(self.name, '\'s finished tasks are: ', self.done_tasks)



tasks_jessika = {'Task-89': 'Done', 'Task-52': 'Not Done', 'Task-8': 'Not Done', 'Task-100': 'Not Done', 'Task-5': 'Done', 'Task-57': 'Done' }
jessica = Employee('Jessica', 'manager', 2500, ['Monday', 'Tuesday', 'Thursday', 'Friday', 'Saturday'], tasks_jessika)
tasks_henry = {'Task-99': 'Not Done', 'Task-152': 'Done', 'Task-88': 'Not Done', 'Task-180': 'Not Done', 'Task-4': 'Done', 'Task-54': 'Not Done' }
henry = Employee('Henry', 'Engineer', 4000, ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], tasks_henry)
print('New position of Jessica is: ', jessica.change_position('Marketing Manager'))
print(henry.is_higher(int(input('write threshold number: '))))
print('Jessica\'s salary per day is: ', jessica.salary_per_day())
print(henry.check_workdays('Monday'))
print(jessica.finished_tasks())
print('count of created employees are: ', Employee.counter)

""""None console-um chem haskanum inchica grum"""
