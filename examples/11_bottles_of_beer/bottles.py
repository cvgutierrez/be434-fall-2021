#!/usr/bin/env python3
"""
Author : caro <caro@localhost>
Date   : 2021-10-25
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Singing the Beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='int',
                        type=int,
                        default=10)

    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    song = []
    for number in range(args.num,0,-1):
        # print(verse(number))
        song.append(verse(number))
    # song = map(verse,range(args.num,0,-1))

    print('\n\n'.join(song))

# --------------------------------------------------
def verse(bottles):
    ''' verse outputs '''
    # return bottles

    if bottles == 1:
        return '\n'.join([
            f'{bottles} bottle of beer on the wall,',
            f'{bottles} bottle of beer,',
            f'Take one down, pass it around,',
            'No bottles of beer on the wall!',
        ])
    else:
        text = "bottle" if bottles == 2 else "bottles"
        return '\n'.join([
            f'{bottles} bottle of beer on the wall,',
            f'{bottles} bottle of beer,',
            f'Take one down, pass it around,',
            f'{bottles -1} {text} of beer on the wall!'
        ])


# --------------------------------------------------
# def test_verse():
#     ''' verse lyrics'''

#     last_lyric = verse(1)



# --------------------------------------------------
if __name__ == '__main__':
    main()
