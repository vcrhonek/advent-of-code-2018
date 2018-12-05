#!/usr/bin/python3

import sys
import string

def react(polymer, removed):
    result = []
    polymer = "".join([char for char in polymer if char.upper() != removed.upper()])
    for c in polymer:
        if result == []:
            result.append(c)
            continue
        if result[-1] != c and result[-1].upper() == c.upper():
             result.pop()
        else:
             result.append(c)
    return len(result)

def main(argv):
    if len(argv) != 2:
        print("Usage: {} INPUT_FILE".format(argv[0]))
        sys.exit(1)


    with open(argv[1], "r", encoding="utf-8") as fin:
        polymer = fin.readline().strip()

    mn = sys.maxsize # hope it's big enough...
    for char in string.ascii_lowercase:
        length = react(polymer, char)
        if length < mn:
            mn = length

    print("The length of the shortest polymer I can produce by removing all units of exactly one type is {}."
           .format(mn))
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
