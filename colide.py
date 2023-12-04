import random

GRID_LENGTH: int = 10

def GetArray(length: int) -> list[list[str]]:
    array: list[list[str]] = []
    length = GRID_LENGTH
    for i in range(length):
        row: list[str] = []
        for j in range(length):
            row.append(None)
        array.append(row)
    return array
    