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
    '''Main Function that calls upon other functions to translate'''

    args = get_args()
    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)
    input_lang = str(args.language1).lower()
    output_lang = str(args.language2).lower()
    front_side = open(os.path.join(args.outdir, input_lang + ".txt"), 'wt')
    back_side = open(os.path.join(args.outdir, output_lang + ".txt"), 'wt')
    together = open(os.path.join(args.outdir,"Side_by_Side.txt"), 'wt')
    flashcards_dict = dict()
    if args.input == None:
        print("There was nothing to translate. Please try again and input either a file or string.")
    elif os.path.isfile(args.input):
        path = os.path.abspath(args.input)
        for line in open(args.input):
            for word in line:
                if word not in flashcards_dict:
                    flashcards_dict[word] = string_translate(word, args.language1, args.language2)
    else:
        words = args.input.split()
        for index in range(len(words)):
            if words[index] not in flashcards_dict:
                flashcards_dict[word] = string_translate(words[index], args.language1, args.language2)


# --------------------------------------------------
def string_translate(string, in_lang, out_lang):
    '''translate strings'''

    interpreter = Translator(from_lang=in_lang.lower(), to_lang=out_lang.lower())
    translation = interpreter.translate(string)
    return translation

  
# --------------------------------------------------
if __name__ == '__main__':
    main()