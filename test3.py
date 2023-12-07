import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def grid_init():
    grid = [["[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]"],
            ]
    return grid

def grid_display(grid):
    clear_screen()
    for row in grid:
        print(''.join(row))

def place_random_numbers(grid):
    empty_cells = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "[ ]"]

    if empty_cells:
        i1, j1 = random.choice(empty_cells)
        empty_cells.remove((i1, j1))
        i2, j2 = random.choice(empty_cells)
        empty_cells.remove((i2, j2))

        grid[i1][j1] = get_numbers()
        grid[i2][j2] = get_numbers()
    else:
        is_game_over(grid)
   

def get_numbers():
    rand_num1 = random.randint(1, 10)

    if rand_num1 <= 9:
        num1 = "[2]"
    else:
        num1 = "[4]"

    return num1
def move_numbers(grid, direction):
    moved = False

    if direction == "z":
        for j in range(len(grid[0])):
            for i in range(1, len(grid)):
                if grid[i][j] != "[ ]":
                    moved |= move_cell(grid, i, j, i - 1, j)

    elif direction == "s":
        for j in range(len(grid[0])):
            for i in range(len(grid) - 2, -1, -1):
                if grid[i][j] != "[ ]":
                    moved |= move_cell(grid, i, j, i + 1, j)

    elif direction == "q":
        for i in range(len(grid)):
            for j in range(1, len(grid[0])):
                if grid[i][j] != "[ ]":
                    moved |= move_cell(grid, i, j, i, j - 1)

    elif direction == "d":
        for i in range(len(grid)):
            for j in range(len(grid[0]) - 2, -1, -1):
                if grid[i][j] != "[ ]":
                    moved |= move_cell(grid, i, j, i, j + 1)

    if moved:
        place_random_numbers(grid)


def move_cell(grid, x, y, new_x, new_y):
    if grid[new_x][new_y] == "[ ]":
        grid[new_x][new_y] = grid[x][y]
        grid[x][y] = "[ ]"
        return True
    elif grid[new_x][new_y] == grid[x][y]:
        merged_value = int(grid[x][y][1]) * 2
        grid[new_x][new_y] = "[{}]".format(merged_value)
        grid[x][y] = "[ ]"
        return True
    return False


def is_game_over(grid):
    is_board_full = not any("[ ]" in (i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] )


# Exemple d'utilisation
grid = grid_init()
place_random_numbers(grid)

while True:
    grid_display(grid)

    move = input("Déplacez avec les touches directionnelles (z/s/q/d) ou 'a' pour quitter: ").lower()

    if move == 'a':
        break
    if is_game_over(grid):
        print("Vous avez perdu ")
        break

    move_numbers(grid, move)
