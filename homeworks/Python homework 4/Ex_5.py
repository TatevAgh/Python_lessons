# *Define a garage collection that stores 3 cars (models), it’s known that double of same models came to garage, print garage models

models = ['bmw', 'audi', 'merc']
new_car1 = input('Write new car model: ')
new_car2 = input('Write new car model: ')
same_models = []
for model in models:
    if new_car1 == model or new_car2 == model:
        same_models.append(model)
print('there isn\'t same models in garage')
if len(same_models) > 0: print(same_models, ' are already in our garage')


