#!/usr/bin/python3

import sys
import re

def main(argv):
    if len(argv) != 2:
        print("Usage: {} INPUT_FILE".format(argv[0]))
        sys.exit(1)

    tstamp_pattern = re.compile("\[\d+-(.*)-(.*) (.*):(.*)\] (.*)")
    guard_pattern = re.compile("Guard #(\d+) begins")

    # key - timestamp MMDDHHMM, value - action at that time
    records = {}
    # just to be sorted...
    tstamps = []
    # key - guard ID, value - list of minutes (0-59) and how
    #   many times the guard sleeped at that particular minute
    guards = {}

    with open(argv[1], "r", encoding="utf-8") as fin:
        for line in fin:
            res = re.search(tstamp_pattern, line.rstrip())
            if res:
                tstamp = int(res.groups()[0] + res.groups()[1]
                             + res.groups()[2] + res.groups()[3])
                tstamps.append(tstamp)
                records[tstamp] = res.groups()[4]

    tstamps.sort()

    fasleep = 0
    for tstamp in tstamps:
        res = re.search(guard_pattern, records[tstamp])
        # guard change?
        if res:
            gid = int(res.groups()[0])
            # guard not in dict yet?
            if not gid in guards:
                guards[gid] = [0 for x in range(60)]
            continue
        # guard falls asleep
        if fasleep == 0:
            fasleep = tstamp
            continue
        # guard wakes up
        else:
            for i in range(tstamp-fasleep):
                guards[gid][fasleep%100 + i] += 1
            fasleep = 0

    # find guard who sleeped the most
    mx = 0
    for guard, times in guards.items():
        minutes = sum(times)
        if minutes > mx:
             gid = guard
             mx = minutes

    print("The ID of the guard you chose multiplied by the minute you chose is {}"
          .format(gid * guards[gid].index(max(guards[gid]))))
                        # index of highest value in list
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
