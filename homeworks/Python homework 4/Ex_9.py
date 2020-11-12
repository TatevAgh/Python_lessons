# *Define a game board (2x2 matrix) with 2 bomb values and 2 gold values, provide user 3 attempts to find all gold values

bomb_game = [['gold', 'bomb'], ['nothing', 'bomb']]
attempts = 3
found = 0
for i in range(attempts):
    board_x = int(input('Write x coodinate until 1: '))
    board_y = int(input('Write y coodinate until 1: '))
    if bomb_game[board_x][board_y] == 'gold':
        found += 1

print('You won the game') if found == 2 else print('You lost')
