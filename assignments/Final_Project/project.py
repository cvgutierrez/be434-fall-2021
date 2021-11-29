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
    
    # parser.add_argument('-f',
    #                     '--file',
    #                     metavar='FILE',
    #                     type=argparse.FileType('rt'),
    #                     help='Input file to translate',
    #                     default=None,
    #                     nargs='*')
    
    # parser.add_argument('-s',
    #                     '--string',
    #                     help="Input string to translate",
    #                     metavar='str',
    #                     type=str,
    #                     default=None,
    #                     nargs='*')
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
    original = open(os.path.join(args.outdir, input_lang + ".txt"), 'wt')
    output = open(os.path.join(args.outdir, output_lang + ".txt"), 'wt')
    together = open(os.path.join(args.outdir,"Side_by_Side.txt"), 'wt')

    if args.input == None:
        print("There was nothing to translate. Please try again and input either a file or string.")
    elif os.path.isfile(args.input):
        path = os.path.abspath(args.input)
        translated = file_translate(path, args.language1, args.language2)
        lines = []
        for line in open(args.input):
            print(line.rstrip(), file= original)
            lines.append(line.rstrip())
        print(translated, file= output)
        combined = [input_lang + ': ' + '\n'.join(lines), '\n', output_lang + ": " + translated]
        print("\n".join(combined), file=together)
    else:
        translated = string_translate(args.input, args.language1, args.language2)
        print(args.input, file=original)
        print(translated, file = output)
        combined = [input_lang + ': ' + args.input, '\n', output_lang + ": " + translated]
        print("\n".join(combined), file=together)


# --------------------------------------------------
def string_translate(string, in_lang, out_lang):
    '''translate strings'''

    interpreter = Translator(from_lang=in_lang.lower(), to_lang=out_lang.lower())
    return interpreter.translate(string)

  
# --------------------------------------------------
def file_translate(input_file, in_lang, out_lang):
    '''translate file'''

    interpreter = Translator(from_lang=in_lang, to_lang=out_lang)
    lines = []
    file = open(input_file, 'rt')
    for line in file:
        # print(line)
        new_line = interpreter.translate(line.rstrip())
        # print(new_line)
        lines.append(new_line)

    return "\n".join(lines)

  
# --------------------------------------------------
if __name__ == '__main__':
    main()