#!/usr/bin/env python3
"""
Author : caro <caro@localhost>
Date   : 2021-11-10
Purpose: Final Project BE 434 Fall 2021
"""

import argparse
import os
from translate import Translator
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate a file or string into a different language with new files as an output in an output directory',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-l1',
                        '--language1',
                        help="Input file's language",
                        metavar='str',
                        type=str,
                        default='Korean')

    parser.add_argument('-l2',
                        '--language2',
                        help="Language the file or string is being translated to",
                        metavar='str',
                        type=str,
                        default='English')

    parser.add_argument('-i',
                        '--input',
                        help="Input to translate",
                        metavar='str',
                        type=str,
                        default=None)
      
    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        type=str,
                        metavar='DIR',
                        default='sys.stdout')

    return parser.parse_args()


# --------------------------------------------------
def main():
    '''Main Function that calls upon other functions to output a romanization of the file in korean'''

    args = get_args()
    romanized = []
    if args.language1.lower() == korean:
        if os.path.isfile(args.input):
            path = os.path.abspath(args.input)
            for line in open(args.input):
                for word in line:
                    romanized.append(romanization(word))


# --------------------------------------------------
def romanization(word):
    '''outputs the romanization of the input or output in korean'''


# --------------------------------------------------
if __name__ == '__main__':
    main()