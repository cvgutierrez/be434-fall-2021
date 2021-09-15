#!/usr/bin/env python3
"""
Author : root <root@localhost>
Date   : 2021-09-14
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('interger',
                        help='intergers to add together',
                        metavar='int',
                        type=int,
                        nargs= '+')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    intergers = args.interger

    returnString = []
    for index in range(len(intergers)):
        returnString.append(str(intergers[index]))
    sumOfIntergers = sum(intergers)
    returnString.append(str(sumOfIntergers))
    if len(returnString) == 2:
        print(' = '.join(returnString))
    else:
        print(' + '.join(returnString[:-1]), '=', sumOfIntergers)

#answer from class
#nums = [string(num) for num in args.interger]
#print('{} = {}' .format( ' + '.join(nums), sum[args.interger]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
