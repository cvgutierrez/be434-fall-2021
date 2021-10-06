#!/usr/bin/env python3
"""
Author : root <root@localhost>
Date   : 2021-10-04
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Counting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=(sys.stdin),
                        nargs='*')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    total_line = 0
    total_word = 0
    total_char = 0
    
    for fh in args.files:
        #print(fh.name)
        line_nums = 0
        word_count = 0
        char_count = 0
        for line in fh:
            line_nums += 1
            #print(line.split())
            word_count += len(line.split())
            char_count += len(line)
        print("{:>8}{:>8}{:>8} {}".format(line_nums, word_count, char_count,
                                    fh.name))
        total_line += line_nums
        total_word += word_count
        total_char += char_count
    #print(fh.name, line_nums, word_count, char_count)
    if len(args.files) >1:
        print("{:>8}{:>8}{:>8}".format(total_line, total_word, 
                                        total_char))



# --------------------------------------------------
if __name__ == '__main__':
    main()
