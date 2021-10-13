#!/usr/bin/env python3
"""
Author : root <root@localhost>
Date   : 2021-10-12
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find what is common between two files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  
    parser.add_argument('FILE1',
                        help='Input file 1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('FILE2',
                        help='Input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--outputfile',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default= sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file1 = args.FILE1
    file2 = args.FILE2

    file1_Contents = file1.read().split()
    file2_Contents = file2.read().split()

    # print(file1_Contents)

    similarities = []
    
    if len(file2_Contents) <= len(file1_Contents):
        for index in range(len(file2_Contents)):
            if file2_Contents[index] in file1_Contents:
                similarities.append(file2_Contents[index])
                # print(file2_Contents[index])
    else:
        for index in range(len(file1_Contents)):
            if file1_Contents[index] in file2_Contents:
                similarities.append(file1_Contents[index])
                # print(file1_Contents[index])    
    
    # print('\n'.join(similarities))
    print('\n'.join(similarities), file=args.outputfile)
    # print('\n'.join(similarities), file=open(args.outputfile, 'wt') if args.outputfile else sys.stdout)
    print(f'Output written to "{args.outputfile.name}".')
    

    


# --------------------------------------------------
if __name__ == '__main__':
    main()
