#!/usr/bin/env python3
"""
Author : root <root@localhost>
Date   : 2021-09-20
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    jumper = {
        '1':'9', 
        '9':'1', 
        '0':'5', 
        '5':'0', 
        '2':'8', 
        '8':'2', 
        '3':'7',
        '7':'3',
        '4':'6',
        '6':'4'
        }
    for char in text:
        # if char in jumper:
        #     print(jumper[char], end='')
        # else:
        #     print(char, end='')
        print(jumper.get(char, char),end='')
    print()


    
# --------------------------------------------------
if __name__ == '__main__':
    main()
