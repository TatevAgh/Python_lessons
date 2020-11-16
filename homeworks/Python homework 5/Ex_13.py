# *Define a collection of color names, generate a new collection
# selecting only color name having more than 1 ‘o’ and print it

colors = ['yellow', 'green', 'orange', 'red', 'cotton candy', 'cordovan']
for color in colors:
    count = 0
    for char in color:
        if char == 'o':
            count += 1
            if count >= 2:
                print(color)
