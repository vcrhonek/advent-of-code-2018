#!/usr/bin/python3

import sys

def main(argv):
    if len(argv) != 2:
        print("Usage: {} INPUT_FILE".format(argv[0]))
        sys.exit(1)

    with open(argv[1], "r", encoding="utf-8") as fin:
        inp = fin.readline().strip().split()
        inp = [int(x) for x in inp]

    nodes = [1]
    meta_cnt = []
    pos = 0
    res = []

    while pos < len(inp):
        # node to store
        if nodes[-1]:
            nodes.append(inp[pos])
            meta_cnt.append(inp[pos+1])
            pos += 2
        # metadata to process
        else:
            res.extend(inp[pos:pos+meta_cnt[-1]])
            pos += meta_cnt[-1]
            meta_cnt.pop()
            nodes.pop()
            nodes[-1] -= 1

    print("The sum of all metadata entries is {}.".format(sum(res)))
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
