import random
import keyboard

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

        num1, num2 = get_number()

        grid[i1][j1] = num1
        grid[i2][j2] = num2



def get_number():
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

def move_up(grid, num1 , num2):
    
        
        
    

def main():
    grid = grid_init()
    place_random_numbers(grid)
    grid_display(grid)    