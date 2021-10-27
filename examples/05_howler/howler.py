#!/usr/bin/env python3
"""
Author : root <root@localhost>
Date   : 2021-09-27
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('howler',
                        help='Howler message from command line',
                        metavar='str',
                        )

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    

    args = parser.parse_args()

    if os.path.isfile(args.howler):
        args.howler = open(args.howler).read().rstrip()
        
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # out_file = open(args.outfile)
    # out_file.write(args.howler.upper())
    #or
    # if args.outfile:
    #     open(args.outfile, 'wt').write(args.howler.upper())
    # else: 
    #     print(args.howler.upper())

    print(args.howler.upper(), file=open(args.outfile, 'wt') if args.outfile else sys.stdout)


# --------------------------------------------------
if __name__ == '__main__':
    main()
