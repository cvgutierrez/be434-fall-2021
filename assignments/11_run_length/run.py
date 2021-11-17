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
                        help='DNA text or file',
                        nargs='+')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # for seq in args.text.splitlines():
    #     print(rle(seq))

    if os.path.isfile(args.text):
        for line in args.text:
            print(rle(line))
    else:
        for seq in args.text:
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

    return ''.join(run)


# --------------------------------------------------
if __name__ == '__main__':
    main()
