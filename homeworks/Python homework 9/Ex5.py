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
        if self.director[0].lower() == symbol:
            print(self.title, 'movie\'s directors name starts from', symbol, 'symbol')
        else:
            print(self.title, 'movie\'s directors name doesn\'t starts from', symbol, 'symbol')

    def is_actor(self, actor):
        if actor in self.actors:
            print(actor, 'exists in', self.title, 'movie\'s actors list')
        else:
            print(actor, 'doesn\'t exists', self.title, 'movie\'s actors list')

    def change_rating(self, new_rating):
        self.rating = new_rating
        return self.rating

actors_gb = ['Mahershala Ali', 'Viggo Mortensen', 'Nick Vallelonga', 'Linda Cardellini']
green_book = Movie('Green Book', 'Peter Farrelly', 130, actors_gb, 8.2)
actors_ff = ['Matt Damon', 'Carroll Shelby', 'Christian Bale', 'Jon Bernthal', 'Caitriona Balfe']
ford_vs_ferrari = Movie('Ford vs ferrari', 'James Mangold', 152, actors_ff, 8.1)
green_book.find_spec_smb('p')
green_book.find_spec_smb('o')
ford_vs_ferrari.is_actor('Mahershala Ali')
green_book.is_actor('Mahershala Ali')
print('new rating for Green book is:', green_book.change_rating(9))

print('Created movies are:', Movie.counter)