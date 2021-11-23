#!/usr/bin/env python3
"""
Author : caro <caro@localhost>
Date   : 2021-11-22
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('PATTERN',
                        metavar='str',
                        help='Search pattern')

    parser.add_argument('FILE',
                        metavar='str',
                        help='Input file(s)')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        metavar='str',
                        type=str,
                        default=False)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output',
                        metavar='FILE',
                        type=argparse.FileType('w'),
                        default=sys.stdout)

    args = parser.parse_args()
    if not os.path.exists(args.FILE):
        parser.error(f"No such file or directory: '{args.FILE}'")

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    if os.path.isfile(args.FILE):
        args.FILE = open(args.FILE, 'r')
    lines = []
    for line in args.FILE:
        if args.insensitive == True:
            if re.search(args.PATTERN, line, re.I):
                lines.append(line.rstrip())
        else:
            if re.search(args.PATTERN, line):
                lines.append(line.rstrip())
    print("\n".join(lines), file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
