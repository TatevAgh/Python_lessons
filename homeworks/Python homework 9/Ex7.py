# Create a class for representing animal,
# create a class for bear and class for wolf, create objects and use them

class Animal:
    def __init__(self, name,  habitat, sex, reproduce, features, food, animal_type):
        self.habitat = habitat
        self.sex = sex
        self.reproduce = reproduce
        self.features = features
        self.food = food
        self.name = name
        self.animal_type = animal_type

    def eating(self):
        print(self.animal_type, 'eats', self.food)

    def presentation_animal(self):
        print('Our animal is a', self.animal_type)



class Bear(Animal):
    def __init__(self, name,  habitat, sex, reproduce, features, food, animal_type, color, zoo_location):
        Animal.__init__(self, name, habitat, sex, reproduce, features, food, animal_type)
        self.color = color
        self.zoo_location = zoo_location




class Wolf(Animal):
    def __init__(self, name,  habitat, sex, reproduce, features, food, animal_type, color, location, position):
        Animal.__init__(self, name, habitat, sex, reproduce, features, food, animal_type)
        self.color = color
        self.location = location
        self.position = position

misha_bear = Bear('Misha', 'land', 'male', 'mammal', ['two legs', 'rich fur'], ['fish', 'meat', 'greens'], 'bear', 'brown', 'moscow zoo',)
hector_wolf = Wolf('Hector', 'forest', 'male', 'mammal', ['four legs', 'predator'], ['other animals', 'meat'], 'wolf', 'gray', 'land', 'alpha',)
misha_bear.eating()
hector_wolf.eating()


