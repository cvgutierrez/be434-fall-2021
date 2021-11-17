#!/usr/bin/env python3
"""
Author : caro <caro@localhost>
Date   : 2021-11-16
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='DNA text or file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    for seq in args.text.splitlines():
        print(rle(seq))

# --------------------------------------------------
def rle(seq):
    """ Create RLE """
    run = []
    run.append(seq[0])
    howmany = 1
    for index in range(1, len(seq)):
        if seq[index] == run[-1]:
            howmany += 1
        elif seq[index] != run[-1] and howmany != 1:
            run.append(str(howmany))
            howmany = 1
            run.append(seq[index])
        else:
            run.append(seq[index])
    if howmany != 1:
        run.append(str(howmany))

    return ''.join(run)


# --------------------------------------------------
if __name__ == '__main__':
    main()
