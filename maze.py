import random
import time
import os


width = int(input("Enter width of maze: "))
height = int(input("Enter hieght of maze: "))
char = '#'
print(char)
if width %2 == 0:
    width +=1
if height%2 == 0:
    height+=1
grid = [[char for i in range(width)] for j in range(height)]

def print_grid(grid):
    grid[1][0] = ' '
    grid[height-2][width-1] = ' '
    for row in grid:
        print(" ".join(row))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def carve_passages_from(cx, cy, grid):
    direction = [0, 1, 2, 3]
    random.shuffle(direction)
    grid[cy][cx] = ' '

    # Print the grid and clear screen for next iteration
    clear_screen()
    print_grid(grid)
    time.sleep(0.05)

    for dir in direction:
        nx = cx + DX[dir]
        ny = cy + DY[dir]
        if 1 <= ny < len(grid) - 1 and 1 <= nx < len(grid[0]) - 1 and grid[ny][nx] == char:
            grid[ny + wallcelly[dir]][nx + wallcellx[dir]] = ' '  # Carve wall
            carve_passages_from(nx, ny, grid)

#     N, E, S, W 
DX = [0, 2, 0, -2]
DY = [-2, 0, 2, 0]
wallcellx = [0, -1, 0, 1]
wallcelly = [1, 0, -1, 0]

carve_passages_from(1, 1, grid)

clear_screen()
print_grid(grid)
