# Create a class for representing a movie with some attributes
# (title, director, duration, actors, rating) and behavior
# (find if movie director name starts with specific symbol, find if some person is an actor, change rating),
# create several movies and perform operations on them, check how many movies are created

class Movie:
    counter = 0

    def __init__(self, title, director, duration, actors, rating):
        self.title = title
        self.director = director
        self.duration = duration
        self.actors = actors
        self.rating = rating
        Movie.counter += 1

    def find_spec_smb(self, symbol):
        if self.director[0] == symbol:
            print(self.title, 'movie\'s directors name starts from', symbol, 'symbol')
        else:
            print(self.title, 'movie\'s directors name doesn\'t starts from', symbol, 'symbol')

    def is_actor(self, actor):
        if actor in self.actors:
            print(actor, 'exists in this movie\'s list')
        else:
            print(actor, 'doesn\'t exists in this movie\'s list')

    def change_rating(self, new_rating):
        self.rating = new_rating
        return self.rating

