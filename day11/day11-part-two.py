#!/usr/bin/python3

import sys

MAX_X = 300
MAX_Y = 300

def compute_cells_power(x, y, grid_sn):
    rack_id = x + 10
    power = (((((rack_id * y) + grid_sn) * rack_id) // 100) % 10) - 5
    return power

def main(argv):
    if len(argv) != 2:
        print("Usage: {} INPUT_FILE".format(argv[0]))
        sys.exit(1)

    with open(argv[1], "r", encoding="utf-8") as fin:
        grid_sn = int(fin.readline().strip())

    grid = []

    # compute power of all cells
    for y in range(MAX_Y):
        for x in range(MAX_X):
            grid.append(compute_cells_power(x+1, y+1, grid_sn))

    # slightly faster, but just few seconds
    grid = tuple(grid)

    # find the largest square and its size
    # it takes ~20 minutes:(
    mx = -sys.maxsize
    coord = None
    best_size = None
    for y in range(MAX_Y):
        for x in range(MAX_X):
            for size in range(1, min(MAX_Y+1-y, MAX_X+1-x)):
               val = 0
               for i in range(size):
                   val += sum(grid[x+(MAX_X*(y+i)):x+(MAX_X*(y+i))+size])
               if val > mx:
                   mx = val
                   coord = (x+1, y+1)
                   best_size = size

    print("The X,Y coordinate of the top-left fuel cell of the {}x{} square with the "
          "largest total power ({}) is {}.\nIts identifier is '{},{},{}'"
          .format(best_size, best_size, mx, coord, coord[0], coord[1], best_size))

    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
