# *Create a collection of flowers with their color, get the flowers which color is red, print result

flowers = {'rose': 'red', 'lisuantus': 'blue', 'sunflower': 'yellow', 'peony': 'red'}
red_flowers = dict(filter(lambda value: value[1] == 'red', flowers.items()))
print('Red flowers: ', red_flowers)