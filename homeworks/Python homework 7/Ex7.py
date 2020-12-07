# *Create several functions store them inside variables for handling collection of movie names using lambdas

collection_movies = ['Bacurau', 'THE GENTLEMEN', 'First Cow', 'Collective', 'THE GREEN BOOK', 'Martin Eden', 'Soul', 'THE OTHER LAMB']

is_the = lambda name: name.lower()[:3] == 'the'
movies_w_the = list(filter(is_the, collection_movies))
print(movies_w_the)
contain_o = lambda name: 'o' in name
movies_w_o = list(filter(contain_o, collection_movies))
print(movies_w_o)

