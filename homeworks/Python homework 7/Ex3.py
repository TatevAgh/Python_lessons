# *Define a collection of company employees (full name(‘Jack Smith’), position),
# calculate how many people with name ‘John’ work in company (create a function),
# calculate how many people have ‘Engineer’ position (create a function), print results

employees = {'Abid Jak': 'Manager', 'John Bailley': 'Accountant', 'Ace Smith': 'Engineer', 'John Jamal': 'Engineer',
             'Jack Smith': 'Engineer', 'Jamaal Smith': 'Bookkeeper'}

def calc_names(people):
    """"Calculates how many Johns are working in company"""
    count = 0
    for employeer in people:
        if 'John' in employeer:
            count += 1
    return count

print('Number of people with name ‘John’ work in company is ', calc_names(employees))

def calc_engineers(people):
    """"Calculates how many Engineers are working in company"""
    count = 0
    for employeer in people.values():
        if 'Engineer' in employeer:
            count += 1
    return count

print('Number of people have ‘Engineer’ position that are working in company is ', calc_engineers(employees))