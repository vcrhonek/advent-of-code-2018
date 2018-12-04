#!/usr/bin/python3

import sys
import re
import numpy as np

def overlaps(fabric, claim):
    xoff = claim[1]
    yoff = claim[2]
    for j in range(claim[4]):
        for i in range(claim[3]):
            # overlaps?
            if fabric[xoff+i, yoff+j] == 2:
                return True
    return False

def main(argv):
    if len(argv) != 2:
        print("Usage: {} INPUT_FILE".format(argv[0]))
        sys.exit(1)

    pattern = re.compile("#(.*) @ (.*),(.*): (.*)x(.*)")

    fabric = np.zeros((1000, 1000))
    claims = []

    with open(argv[1], "r", encoding="utf-8") as fin:
        for line in fin:
            res = re.search(pattern, line.rstrip())
            if res:
                claims.append((res.groups()[0], int(res.groups()[1]), int(res.groups()[2]),
                              int(res.groups()[3]), int(res.groups()[4])))

    for claim in claims:
        xoff = claim[1]
        yoff = claim[2]
        for j in range(claim[4]):
             for i in range(claim[3]):
                # already claimed?
                if fabric[xoff+i, yoff+j]:
                    # claimed by one?
                    if fabric[xoff+i, yoff+j] == 1:
                        fabric[xoff+i, yoff+j] = 2
                else:
                    fabric[xoff+i, yoff+j] = 1

    for claim in claims:
        if not overlaps(fabric, claim):
            print("The ID of the only claim that doesn't overlap is {}.".format(claim[0]))
            break

    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
