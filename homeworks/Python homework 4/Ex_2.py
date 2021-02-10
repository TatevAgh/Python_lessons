# *Define a collection of colors, add a color from console, print total colors number, print colors on even positions

colors = ['blue', 'green', 'red', 'yellow']
add_color = input('Add a color: ')
colors.append(add_color)
print('total colors number: ', len(colors))
print('colors on even positions: ', colors[1::2])