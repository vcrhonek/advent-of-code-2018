#!/usr/bin/python3

import sys

def main(argv):
    if len(argv) != 2:
        print("Usage: {} INPUT_FILE".format(argv[0]))
        sys.exit(1)

    freq = 0
    with open(argv[1], "r", encoding="utf-8") as fin:
        for line in fin:
            change = int(line.rstrip())
            freq += change

    print("Resulting frequency is {}.".format(freq))
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
