import random
import os
import time

sleepingTime = 0.1
GRID_SIZE = 11

class point:
    def __init__(self):
        self.hasTreasure = False
        self.isVisited = False
        self.isPerson = False

def printGrid(grid, showTreasure=False):
    os.system('clear')  # Clear the terminal
    for row in grid:
        for cell in row:
            if cell.isPerson and not showTreasure:
                print("P", end=" ")
            elif cell.hasTreasure and showTreasure:
                print("$", end=" ")
            elif cell.isVisited:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

def spiralSearch(grid, startRow, startCol):
    directions = [(-1,0), (0,1), (1,0), (0,-1)]  # up, right, down, left
    steps = 1
    row, col = startRow, startCol
    grid[row][col].isPerson = True
    grid[row][col].isVisited = True
    printGrid(grid)
    time.sleep(sleepingTime)
    found = False

    while steps < GRID_SIZE:
        for d in range(2):  # two times for each step size
            dr, dc = directions[0]
            directions = directions[1:] + directions[:1]  # rotate directions
            for _ in range(steps):
                row += dr
                col += dc
                if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                    # Move person
                    for r in range(GRID_SIZE):
                        for c in range(GRID_SIZE):
                            grid[r][c].isPerson = False
                    grid[row][col].isPerson = True
                    grid[row][col].isVisited = True
                    if grid[row][col].hasTreasure:
                        printGrid(grid, showTreasure=True)
                        print(f"Treasure found at ({row}, {col})!")
                        found = True
                        print(f"Treasure position: ({row}, {col})")
                        return
                    else:
                        printGrid(grid)
                        time.sleep(sleepingTime)
        steps += 1

    # Final outer ring
    dr, dc = directions[0]
    for _ in range(steps):
        row += dr
        col += dc
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            for r in range(GRID_SIZE):
                for c in range(GRID_SIZE):
                    grid[r][c].isPerson = False
            grid[row][col].isPerson = True
            grid[row][col].isVisited = True
            if grid[row][col].hasTreasure:
                printGrid(grid, showTreasure=True)
                print(f"Treasure found at ({row}, {col})!")
                found = True
                print(f"Treasure position: ({row}, {col})")
                return
            else:
                printGrid(grid)
                time.sleep(sleepingTime)
    if not found:
        print("Treasure not found.")

treasureField = [[point() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

treasureRow = random.randint(0, GRID_SIZE - 1)
treasureCol = random.randint(0, GRID_SIZE - 1)
center = GRID_SIZE // 2
while treasureRow == center and treasureCol == center:
    treasureRow = random.randint(0, GRID_SIZE - 1)
    treasureCol = random.randint(0, GRID_SIZE - 1)
treasureField[0][0].hasTreasure = True

personRow = center
personCol = center

spiralSearch(treasureField, personRow, personCol)
