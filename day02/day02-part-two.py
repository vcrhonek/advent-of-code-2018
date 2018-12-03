#!/usr/bin/python3

import sys
import regex

def scan(box_id, box_id_lst):
    for q in box_id_lst:
        # don't process identical IDs
        if q == box_id:
            continue
        # search for just one substitution
        m = regex.search(r'(%s){s<=1}'%q, box_id)
        if m:
            # found, get index of character that differs
            index_lst, _, _ = m.fuzzy_changes
            return index_lst[0]
    return None


def main(argv):
    if len(argv) != 2:
        print("Usage: {} INPUT_FILE".format(argv[0]))
        sys.exit(1)

    box_id_lst = []

    with open(argv[1], "r", encoding="utf-8") as fin:
        for line in fin:
            box_id_lst.append(line.rstrip())

    for box_id in box_id_lst:
        index = scan(box_id, box_id_lst)
        if index is not None:
          print("Common letters between the two correct box IDs are '{}{}'"
                .format(box_id[:index], box_id[index+1:]))
          break

    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
