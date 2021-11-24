#!/usr/bin/env python3
"""
Author : root <root@localhost>
Date   : 2021-09-21
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
                        help='Do-Re-Mi',
                        nargs='+',
                        metavar='str',
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    Song = {
        'Do':'A deer, a female deer',
        'Re':'A drop of golden sun',
        'Mi':'A name I call myself',
        'Fa':'A long long way to run',
        'Sol':'A needle pulling thread',
        'La':'A note to follow sol',
        'Ti':'A drink with jam and bread'
        }
    for index in range(len(text)):
        if text[index] in Song:
            print((text[index]+','), Song.get(text[index]), end='')
            print()
        else:
            print("I don't know", '"' + text[index] + '"')
    # for index in range(len(text)):
    #     print((text[index]+','), Song.get(text[index], ("I don't know " + text[index])),end='')
    #     print()
    # Can't figure out how to just print I don't know Foo instead of Foo, I don't know Foo


# --------------------------------------------------
if __name__ == '__main__':
    main()
