import random

def grid_init():
    grid = [["[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]"],
            ["[ ]", "[ ]", "[ ]", "[ ]"]
            ]
    return grid

def grid_display(grid):
    i = 0
    row_count : int = len(grid)
    while i < row_count:
        j = 0
        col_count = len(grid[i]) 
        while j < col_count:
            print(grid[i][j], end="")
            j += 1

        print("\n")

        i += 1

def place_random_numbers(grid):
    empty_cells = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "[ ]"]

    if empty_cells:
        i1, j1 = random.choice(empty_cells)
        empty_cells.remove((i1, j1))
        i2, j2 = random.choice(empty_cells)

        num1, num2 = get_numbers()

        grid[i1][j1] = num1
        grid[i2][j2] = num2

def move_numbers(grid, direction):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if "[2]" in grid[i][j] or "[4]" in grid[i][j]:
                x, y = i, j
                break

    if (
        (direction == "w" and y > 0)
        or (direction == "s" and y < 3)
        or (direction == "a" and x > 0)
        or (direction == "d" and x < 3)
    ):
        # Déplacer le point
        grid[x][y] = "[ ]"
        if direction == "w":
            y = 0
        elif direction == "s":
            y =+ 3
        elif direction == "a":
            x = 0
        elif direction == "d":
            x = 3

        return grid[x][y]

    place_random_numbers(grid)

def get_numbers():
    rand_num1 = random.randint(1, 10)
    rand_num2 = random.randint(1, 10)

    if rand_num1 <= 9:
        num1 = "[2]"
    else:
        num1 = "[4]"

    if rand_num2 <= 9:
        num2 = "[2]"
    else:
        num2 = "[4]"

    return num1, num2


# Exemple d'utilisation
grid = grid_init()
place_random_numbers(grid)
grid_display(grid)

while True:
    move = input("Déplacez avec les touches directionnelles (w/s/a/d) ou 'q' pour quitter: ").lower()

    if move == 'q':
        break

    move_numbers(grid, move)
    grid_display(grid)
