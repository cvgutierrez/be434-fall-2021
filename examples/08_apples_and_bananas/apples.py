#!/usr/bin/env python3
"""
Author : root <root@localhost>
Date   : 2021-10-11
Purpose: Rock the Casbah
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Replacing vowels with other vowels',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='Vowel to replace',
                        metavar='str',
                        type=str,
                        default='a',
                        choices=list('aeiou'))

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    # if args.vowel.lower() not in 'aeiou':
    #     parser.error(f'--vowel "{args.vowel}" is not a vowel')

    return args



# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    

    print(args)

    new_text = ""
    for char in args.text:
        if char in "aeiou":
            new_text += args.vowel
        elif char in "AEIOU":
            new_text += args.vowel.upper
        else:
            new_text += char
        # print(new_text)

    text = args.text
    text = re.sub('[aeiou]', args.vowel, text)
    text = re.sub('[AEIOU]', args.vowel.upper(), text)
    
    print(new_text)
    print(args.text)
    print(text)
    # return new_text



# --------------------------------------------------
if __name__ == '__main__':
    main()
