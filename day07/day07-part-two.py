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
    TAKES = 60
    WORKERS = 5

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

    # initialize workers, "." - idle, "X" - works on X
    jobs = ["." for x in range(WORKERS)]
    # initialize durations of jobs per worker
    durations = [0 for x in range(WORKERS)]

    total_time = 0
    # finish only when nothing in available and all workers are idle
    while available != [] or len(set(jobs)) != 1:
        # assign work to idle workers
        for i in range(WORKERS):
            if jobs[i] == "." and available != []:
                jobs[i] = available.pop(0)
                durations[i] = TAKES + nodes.index(jobs[i]) + 1

        # finish fastest job
        mn = sys.maxsize
        for i in range(WORKERS):
            if jobs[i] != ".":
                if durations[i] < mn:
                    mn = durations[i]
                    wid = i
        order += jobs[wid]
        jobs[wid] = "."
        total_time += mn

        # move time in jobs of other workers
        for i in range(WORKERS):
            if jobs[i] != ".":
                durations[i] -= mn

        if not order[-1] in leads:
            # this node is dead end, skip to next available
            continue
        # check every node we can go from current node
        for node in leads[order[-1]]:
            # check whether all requires are fulfilled
            fulfilled = True
            for require in requires[node]:
                if require not in order:
                      # require not fulfilled, skip node
                      fulfilled = False
                      break
            if fulfilled:
                # all requires fulfilled, add node to available
                if node not in available and node not in order:
                    available.append(node)
        available.sort()

    print("The steps in my instructions should be completed in this order: {}. It took {} seconds to complete."
          .format(order, total_time))
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
