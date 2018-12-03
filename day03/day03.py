#!/usr/bin/python3

import sys
import re
import numpy as np

def main(argv):
    if len(argv) != 2:
        print("Usage: {} INPUT_FILE".format(argv[0]))
        sys.exit(1)

    pattern = re.compile("#*@ (.*),(.*): (.*)x(.*)")

    fabric = np.zeros((1000, 1000))

    with open(argv[1], "r", encoding="utf-8") as fin:
        for line in fin:
            res = re.search(pattern, line.rstrip())
            if res:
                xoff = int(res.groups()[0])
                yoff = int(res.groups()[1])
                for j in range(int(res.groups()[3])):
                    for i in range(int(res.groups()[2])):
                        # already claimed?
                        if fabric[xoff+i, yoff+j]:
                            # claimed by one?
                            if fabric[xoff+i, yoff+j] == 1:
                                fabric[xoff+i, yoff+j] = 2
                        else:
                            fabric[xoff+i, yoff+j] = 1

    print("{} square inches of fabric are within two or more claims.".format(np.count_nonzero(fabric == 2)))
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
