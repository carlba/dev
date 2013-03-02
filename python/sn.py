#!/usr/bin/env python
"""simplenote command line app"""

import sys
import fileinput

from simplenote import Simplenote
sn = Simplenote("genzorg@gmail.com", "bajskorv")

def send(txt):
    note = {'content': txt}
    note, status = sn.add_note(note)

    if status != 0:
        print >> sys.stderr, note
        sys.exit(1)


def read_until_dot():
    line = raw_input()
    while line != ".":
        yield line
        line = raw_input()

import sys
def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) == 1:
        lines = read_until_dot()
    else:
        lines = fileinput.input()

    send("\n".join(lines))


if __name__ == '__main__':
    main()