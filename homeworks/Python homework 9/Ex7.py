# Create a class for representing animal,
# create a class for bear and class for wolf, create objects and use them

class Animal:
    def __init__(self, habitat, sex, reproduce, features, food):
        self.habitat = habitat
        self.sex = sex
        self.reproduce = reproduce
        self.features = features
        self.food = food


class Bear(Animal):
    def __init__(self, name, habitat, sex, reproduce, features, color, zoo_location, food):
        Animal.__init__(self, habitat, sex, reproduce, features, food)
        self.name = name
        self.color = color
        self.zoo_location = zoo_location

class Wolf(Animal):
    def __init__(self, name, habitat, sex, reproduce, features, color, location, position, food):
        Animal.__init__(self, habitat, sex, reproduce, features, food)
        self.name = name
        self.color = color
        self.location = location
        self.position = position

misha_bear = Bear('Misha', 'land', 'male', 'mammal', ['two legs', 'rich fur'], 'brown', 'moscow zoo', ['fish', 'meat', 'greens'])



