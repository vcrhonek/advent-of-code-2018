#!/usr/bin/python3

import sys
import numpy as np

MAX_X = 300
MAX_Y = 300
SIZE = 3

def compute_cells_power(x, y, grid_sn):
    rack_id = x + 10
    power = (((((rack_id * y) + grid_sn) * rack_id) // 100) % 10) - 5
    return power

def compute_square(x, y, size, grid):
    return sum(grid[y:y+size, x:x+size].flat)

def main(argv):
    if len(argv) != 2:
        print("Usage: {} INPUT_FILE".format(argv[0]))
        sys.exit(1)

    with open(argv[1], "r", encoding="utf-8") as fin:
        grid_sn = int(fin.readline().strip())

    grid = np.zeros((MAX_Y,MAX_X), dtype=int)

    # compute power of all cells
    for y in range(MAX_Y):
        for x in range(MAX_X):
            grid[y, x] = compute_cells_power(x+1, y+1, grid_sn)

    # find the 3x3 square which has the largest total power
    mx = -sys.maxsize
    coord = None
    for y in range(MAX_Y):
        for x in range(MAX_X):
            val = compute_square(x, y, SIZE, grid)
            if val > mx:
                mx = val
                coord = (x+1, y+1)

    print("The X,Y coordinate of the top-left fuel cell of the 3x3 square with the "
          "largest total power ({}) is {}.\nIts dentifier is '{},{}'"
          .format(mx, coord, coord[0], coord[1]))

    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
