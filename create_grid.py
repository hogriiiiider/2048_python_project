import random 

def grid_init():
    grid = []
    for row in range(4):
        grid.append([''] * 4)
    return grid

def grid_display(grid):
    for row in grid:
        print('  '.join(map(str, row)))

def get_number():
    rand_num = random.randint(1, 10)
    if rand_num <= 9:
        return 2
    else:
        return 4
    
grid = grid_init()  # Correction ici : grid_init() au lieu de grid_init

for i in range(4):
    grid_display(grid)
