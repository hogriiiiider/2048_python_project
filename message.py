import random
import os
import keyboard

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
        for cell in row:
            print(cell, end="")
        print()

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

def move(grid, direction):
    pos_num = [["[ ]" for _ in range(len(grid[0]))] for _ in range(len(grid))]

    if direction == "up":
        for j in range(len(grid[0])):
            nums = [grid[i][j] for i in range(len(grid))]
            nums = [num for num in nums if num != "[ ]"]
            for i in range(len(nums)):
                pos_num[i][j] = nums[i]

    elif direction == "down":
        for j in range(len(grid[0])):
            nums = [grid[i][j] for i in range(len(grid))]
            nums = [num for num in nums if num != "[ ]"]
            for i in range(len(nums)):
                pos_num[len(grid) - len(nums) + i][j] = nums[i]

    elif direction == "left":
        for i in range(len(grid)):
            nums = grid[i]
            nums = [num for num in nums if num != "[ ]"]
            for j in range(len(nums)):
                pos_num[i][j] = nums[j]

    elif direction == "right":
        for i in range(len(grid)):
            nums = grid[i]
            nums = [num for num in nums if num != "[ ]"]
            for j in range(len(nums)):
                pos_num[i][len(grid[0]) - len(nums) + j] = nums[j]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = pos_num[i][j]


def main():
    grid = grid_init()
    place_random_numbers(grid)
    
    while True:
        clear_screen()
        grid_display(grid)

        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN and event.name == "z":
            move(grid, "up")

        if event.event_type == keyboard.KEY_DOWN and event.name == "q":
            move(grid, "left")

        if event.event_type == keyboard.KEY_DOWN and event.name == "s":
            move(grid, "down")

        if event.event_type == keyboard.KEY_DOWN and event.name == "d":
            move(grid, "right")


main()