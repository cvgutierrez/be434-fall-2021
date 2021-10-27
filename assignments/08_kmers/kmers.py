#!/usr/bin/env python3
"""
Author : caro <caro@localhost>
Date   : 2021-10-26
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common k-mers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-k',
                        '--kmer',
                        help='kmer length',
                        metavar='int',
                        type=int,
                        default=3)

    parser.add_argument('FILE1',
                        help='Input file 1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('FILE2',
                        help='Input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        default=None)

    args = parser.parse_args()
    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be greater than 0')
    
    if os.path.isfile(args.FILE1.name) == False:
        parser.error(f"argument FILE1: can't open '{args.FILE1.name}'")
    
    if os.path.isfile(args.FILE2.name) == False:
        parser.error(f"argument FILE2: can't open '{args.FILE2.name}'")

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    file1_dictionary = Dictionaries(args.FILE1, args.kmer)
    file2_dictionary = Dictionaries(args.FILE2, args.kmer)

    Similarities(file1_dictionary, file2_dictionary)
    

# --------------------------------------------------
def Dictionaries(file, kmer):
    """Create dictionaries of kmers with number of occurances"""

    file_Contents = ''.join(file.read().split())
    # print(file_Contents)

    file_Dictionary = dict()

    listOfKmers = []
    for i in range (0, len(file_Contents) -(kmer-1)):
        listOfKmers.append(file_Contents[i:i+kmer])
        print(file_Contents[i:i+kmer])

    for index in range(len(listOfKmers)):
        if listOfKmers[index] in file_Dictionary:
            file_Dictionary[listOfKmers[index]] = file_Dictionary[listOfKmers[index]] + 1
        else:
            file_Dictionary[listOfKmers[index]] = 1

    # print(file_Dictionary)

    return file_Dictionary


# --------------------------------------------------
def Similarities(file1, file2):
    """Find similarities and print the occurances"""

    similarKmers = []
    for key in file1:
        if key in file2:
            similarKmers.append(key)
            if key in similarKmers:
                print(f'{key} {file1.get(key):10} {file2.get(key):5}')

    

# --------------------------------------------------
if __name__ == '__main__':
    main()
