#!/usr/bin/python3

import sys
import numpy as np

def main(argv):
    if len(argv) != 2:
        print("Usage: {} INPUT_FILE".format(argv[0]))
        sys.exit(1)

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
            # ...compute distance to all coordinates
            distances = {}
            for coord_id in coords:
               distances[coord_id] = abs(x - coords[coord_id][0]) + abs(y - coords[coord_id][1])
            # find lowest unique (lowest non-unique let remain zero)
            vals = distances.values()
            min_val = min(vals)
            min_vals = []
            for coord_id in distances.keys():
                if distances[coord_id] == min_val:
                    min_vals.append(coord_id)
            if len(min_vals) == 1:
                locations[x][y] = min_vals[0]
            else:
                locations[x][y] = 0

    # count max area, the value must not be on the edge
    mx = 0
    for coord_id in distances.keys():
        # do not count edges
        if coord_id in locations[0, :] or coord_id in locations[X-1, :] or coord_id in locations[:, 0] or coord_id in locations[:, Y-1]:
            continue
        cnt = np.count_nonzero(locations == coord_id)
        if cnt > mx:
            mx = cnt

    print("The size of the largest area that isn't infinite is {}.".format(mx))
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
