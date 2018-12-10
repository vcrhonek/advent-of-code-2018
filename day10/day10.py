#!/usr/bin/python3

import sys
import re
import numpy as np
import os

MATRIX_SIZE = 500
THRESHOLD_X = 100
THRESHOLD_Y = 100

def main(argv):
    if len(argv) != 2:
        print("Usage: {} INPUT_FILE".format(argv[0]))
        sys.exit(1)

    pattern = re.compile("position=<(.*),(.*)> velocity=<(.*),(.*)>")
    points = []
    velocities = []

    with open(argv[1], "r", encoding="utf-8") as fin:
        for line in fin:
            res = re.search(pattern, line.strip())
            if res:
                x, y, vx, vy = int(res.groups()[0].strip()), int(res.groups()[1].strip()), int(res.groups()[2].strip()), int(res.groups()[3].strip())
                points.append([x, y])
                velocities.append((vx, vy))

    time = 0
    while True:
        condensed = False
        mnx, mxx, mny, mxy = sys.maxsize, -sys.maxsize, sys.maxsize, -sys.maxsize
        for idx, point in enumerate(points):
            point[0] += velocities[idx][0]
            point[1] += velocities[idx][1]
            mnx, mxx, mny, mxy = min(mnx, point[0]), max(mxx, point[0]), min(mny, point[1]), max(mxy, point[1])
        time += 1
        if mxy-mny < THRESHOLD_Y and mxx-mnx < THRESHOLD_X:
            condensed = True
        if condensed:
            sky = np.zeros((MATRIX_SIZE,MATRIX_SIZE))
            for idx, point in enumerate(points):
                sky[point[1]][point[0]] = 1
            os.system('clear')
            y = 0
            for row in sky:
                if y >= mny and y <= mxy:
                    x = 0
                    for i in row:
                        if x >= mnx and x <= mxx:
                            if i:
                                print("#", end="")
                            else:
                                print(" ", end="")
                        x += 1
                    print()
                y += 1
            print("Seconds needed to wait for the message to appear: {}".format(time))
            x = input()


    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
