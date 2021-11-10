#!/usr/bin/env python3
"""
Author : caro <caro@localhost>
Date   : 2021-11-10
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('File',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs="+")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    lines = []
    for fh in args.File:
        for line in fh:
            lines.append(line.rstrip())     
    same_bases = list(lines[0])
    for _ in range(len(lines)-1):
        for index in range(len(same_bases)):
            if same_bases[index] != 'X':
                if lines[_][index] == lines[_+1][index]:
                    same_bases[index] = '|'
                else:
                    same_bases[index] = 'X'  
    print('\n'.join(lines))
    print(''.join(same_bases))


# --------------------------------------------------
if __name__ == '__main__':
    main()
