#!/usr/bin/python3

import sys
import re

def main(argv):
    if len(argv) != 2:
        print("Usage: {} INPUT_FILE".format(argv[0]))
        sys.exit(1)

    pattern = re.compile("Step (.) must be finished before step (.) can begin.")
    leads = {}
    requires = {}
    letters = set()

    with open(argv[1], "r", encoding="utf-8") as fin:
        for line in fin:
            res = re.search(pattern, line.strip())
            if res:
                leads.setdefault(res.groups()[0], []).append(res.groups()[1])
                requires.setdefault(res.groups()[1], []).append(res.groups()[0])
                letters.update(res.groups()[0], res.groups()[1])

    
    # get sorted list of nodes from set of letters
    nodes = [x for x in letters]
    nodes.sort()

    # sort leads and requires
    for _, item in leads.items():
        item.sort()
    for _, item in requires.items():
        item.sort()

    # find list of nodes without requirements - starting nodes
    available = []
    order = ""
    for letter in letters:
        if letter not in requires:
            available.append(letter)
    available.sort()

    while available != []:
        order += available.pop(0)
        if not order[-1] in leads:
            # this node is dead end, skip to next avaialbe
            continue
        # check every node we can go from current node
        for node in leads[order[-1]]:
            # check whether are requires ale fullfiled
            fullfiled = True
            for require in requires[node]:
                if require not in order:
                      # require not fullfiled, skip node
                      fullfiled = False
                      break
            if fullfiled:
                # all requires fullfiled, add node to available
                if node not in available and node not in order:
                    available.append(node)
        available.sort()

    print("The steps in my instructions should be completed in this order: {}"
          .format(order))
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
