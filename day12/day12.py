#!/usr/bin/python3

import sys

MAGIC = 4
GENERATIONS = 20

def main(argv):
    if len(argv) != 2:
        print("Usage: {} INPUT_FILE".format(argv[0]))
        sys.exit(1)

    rules = {}

    with open(argv[1], "r", encoding="utf-8") as fin:
        line = fin.readline().strip().split()
        pots = line[-1]
        line = fin.readline()
        for line in fin:
            rules[line.strip().split()[0]] = line.strip().split()[-1]

    generation = 0
    pot_zero = 0
    while generation < GENERATIONS:
        if "#" in pots[:4]:
            pots = "." * MAGIC + pots
            pot_zero += 4
        if "#" in pots[-4:]:
            pots = pots + MAGIC * "."
        updated_pots = ["." for x in range(len(pots))]
        for idx in range(len(pots)):
            for rule in rules:
                if pots[idx:idx+5] == rule:
                     updated_pots[idx+2] = rules[rule]
        pots = "".join(updated_pots)
        generation += 1

    total = 0
    for i in range(pot_zero, len(pots)):
        if pots[i] == "#":
            total += (i-pot_zero)
    for i in range(pot_zero, -1, -1):
        if pots[i] == "#":
            total -= (pot_zero-i)

    print("After {} generations, the sum of the numbers of all pots which contain a plant is {}."
          .format(GENERATIONS, total))
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
