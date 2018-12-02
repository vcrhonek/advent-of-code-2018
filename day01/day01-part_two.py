#!/usr/bin/python3

import sys
import itertools

def main(argv):
    if len(argv) != 2:
        print("Usage: {} INPUT_FILE".format(argv[0]))
        sys.exit(1)

    freq = 0
    inp_lst = []
    # use set - no duplicates, saves resources
    freq_hist = {0}

    with open(argv[1], "r", encoding="utf-8") as fin:
        for line in fin:
            inp_lst.append(int(line.rstrip()))

    # itertools.cycle - cycles over iterable forever
    for change in itertools.cycle(inp_lst):
        freq += change
        if freq in freq_hist:
            break
        freq_hist.add(freq)

    print("First frequency reached twice is {}.".format(freq))
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
