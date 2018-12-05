#!/usr/bin/python3

import sys

def main(argv):
    if len(argv) != 2:
        print("Usage: {} INPUT_FILE".format(argv[0]))
        sys.exit(1)

    polymer = []

    with open(argv[1], "r", encoding="utf-8") as fin:
        while True:
            c = fin.read(1)
            if not c or c == '\n':
                break
            if polymer == []:
                polymer.append(c)
                continue
            if polymer[-1] != c and polymer[-1].upper() == c.upper():
                polymer.pop()
            else:
                polymer.append(c)

    print("There remains {} units after fully reacting the polymer I scanned.".format(len(polymer)))
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
