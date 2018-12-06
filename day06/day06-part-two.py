#!/usr/bin/python3

import sys
import numpy as np

def main(argv):
    if len(argv) != 2:
        print("Usage: {} INPUT_FILE".format(argv[0]))
        sys.exit(1)

    THRESHOLD = 10000
    X = 500
    Y = 500
    locations = np.zeros((X, Y))
    coords = {}
    coord_id = 1

    with open(argv[1], "r", encoding="utf-8") as fin:
        for line in fin:
           x, y = line.strip().split(',')
           locations[int(x)][int(y)] = coord_id
           coords[coord_id] = [int(x), int(y)]
           coord_id += 1

    # for every location in grid...
    for x in range(X):
        for y in range(Y):
            # ...compute distance to all coordinates and make a sum of it
            total = 0
            for coord_id in coords:
               total +=  abs(x - coords[coord_id][0]) + abs(y - coords[coord_id][1])
            locations[x][y] = total

    # just count the number of locations which have sum lower than desired threshold
    cnt = np.count_nonzero(locations < THRESHOLD)

    print("The size of the region containing all locations which have a total distance to all given coordinates of less than {} is {}."
          .format(THRESHOLD, cnt))
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
