# *Create a collection of 6 names inputed from console ,
# generate a new collection selecting only the names starting from ‘A’ and print it

names = []
names_started_a = []
while len(names) != 6:
    names.append(input('Write a name: '))

for name in names:
    if name[0] == 'a':
        names_started_a.append(name)

print('This is names: ', names)
print('This is names started with `a`: ', names_started_a)