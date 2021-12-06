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

    parser.add_argument('file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--number',
                        help='Line numbers',
                        action='store_true',
                        default=False)

    args = parser.parse_args()

    # if os.path.isfile(args.file.name):
    #     args.file = open(args.file.name).read().rstrip()
    #     print(args.file)
    # if not os.path.isfile(args.file):
    #     parser.error(f'No such file or directory: "{args.file.name}"')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for fh in args.file:
        lines = open(args.file.name, 'rt')
        nums = 1
        if len(fh) <1:
            nums = 1
        else:
            for line in lines:
                if args.number:
                    new_line = '     ' + str(nums) + '	' + line.rstrip()
                    print(new_line)
                    nums +=1
                else:
                    print(line.rstrip())


# --------------------------------------------------
if __name__ == '__main__':
    main()
