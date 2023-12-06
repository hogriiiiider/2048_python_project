
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def grid_init():
    grid = [["[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]"]
            ]
    return grid

def grid_display(grid):
    for row in grid:
        print(''.join(row))

def place_random_numbers(grid):
    empty_cells = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "[ ]"]

    if empty_cells:
        i1, j1 = random.choice(empty_cells)
        empty_cells.remove((i1, j1))
        i2, j2 = random.choice(empty_cells)

        grid[i1][j1] = get_numbers()
        grid[i2][j2] = get_numbers()

def get_numbers():
    rand_num1 = random.randint(1, 10)

    if rand_num1 <= 9:
        num1 = "[2]"
    else:
        num1 = "[4]"

    return num1

def collide_cells(grid, x, y, direction):
    new_x, new_y = x, y

    if direction == "w" and y > 0:
        new_y = y - 1
    elif direction == "s" and y < 3:
        new_y = y + 1
    elif direction == "a" and x > 0:
        new_x = x - 1
    elif direction == "d" and x < 3:
        new_x = x + 1

    if grid[new_x][new_y] == "[ ]":
        return new_x, new_y
    else:
        return x, y

def move_numbers(grid, direction):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if "[2]" in grid[i][j] or "[4]" in grid[i][j]:
                x, y = i, j
                break

    new_x, new_y = collide_cells(grid, x, y, direction)

    # Déplacer le point
    grid[new_x][new_y] = grid[x][y]
    #place_random_numbers(grid)

# Exemple d'utilisation
grid = grid_init()
place_random_numbers(grid)
grid_display(grid)

while True:
    grid_display(grid)

    move = input("Déplacez avec les touches directionnelles (w/s/a/d) ou 'q' pour quitter: ").lower()

    if move == 'q':
        break

    move_numbers(grid, move)
