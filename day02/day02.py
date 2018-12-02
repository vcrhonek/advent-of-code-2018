#!/usr/bin/python3

import sys
import string

def scan(box_id, rate):
    for letter in string.ascii_lowercase:
        if letter in box_id:
            if box_id.count(letter) == rate:
                return True
    return False


def main(argv):
    if len(argv) != 2:
        print("Usage: {} INPUT_FILE".format(argv[0]))
        sys.exit(1)

    twice = 0
    thrice = 0

    with open(argv[1], "r", encoding="utf-8") as fin:
        for line in fin:
            box_id = line.rstrip()
            if scan(box_id, 2):
                twice += 1
            if scan(box_id, 3):
                thrice += 1

    print("The checksum is {}.".format(twice * thrice))
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
