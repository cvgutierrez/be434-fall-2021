#!/usr/bin/env python3
"""
Author : root <root@localhost>
Date   : 2021-09-28
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Printing and or Counting Lines of Files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-n',
                        '--number',
                        help='Line numbers',
                        action='store_true')

    args = parser.parse_args()

    if os.path.isfile(args.file):
        args.file = open(args.file).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    fh = open(args.file, 'wt') if args.file else sys.stdout
    nums = 1
    for line in fh:
        if -n:
            fh.write(nums, args.file)
            nums +=1
        else:
            fh.write(args.file)

    fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
