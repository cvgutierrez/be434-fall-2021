#!/usr/bin/env python3
"""
Author : caro <caro@localhost>
Date   : 2021-10-26
Purpose: Rock the Casbah
"""

import argparse


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
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    kmers1 = count_kmers(args.FILE1, args.kmer)
    kmers2 = count_kmers(args.FILE2, args.kmer)

    for common in set(kmers1).intersection(set(kmers2)):
        print('{:10}{:6}{:6}'.format(common, kmers1.get(common),
                                     kmers2.get(common)))

    # for kmer in kmers1:
    #     if kmer in kmers2:
    #         print(kmer, kmers1.get(kmer), kmers2.get(kmer))

    # file1_dictionary = Dictionaries(args.FILE1, args.kmer)
    # file2_dictionary = Dictionaries(args.FILE2, args.kmer)

    # Similarities(file1_dictionary, file2_dictionary)


# --------------------------------------------------
def find_kmers(seq, k):
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------
def count_kmers(file, k):
    '''Makes dictionaries of kmers for each file'''

    kmers = {}
    for line in file:
        for word in line.split():
            for kmer in find_kmers(word, k):
                if kmer not in kmers:
                    kmers[kmer] = 0
                kmers[kmer] += 1

    return kmers


# # --------------------------------------------------
# def Dictionaries(file, kmer):
#     """Create dictionaries of kmers with number of occurances"""

#     file_Dictionary = dict()

#     listOfKmers = []
#
#   for line in file:
#       for i in range(line - kmer + 1):
#         listOfKmers.append(file[i:i + kmer])

#     for index in range(len(listOfKmers)):
#         if listOfKmers[index] in file_Dictionary:
#             file_Dictionary[listOfKmers[index]] = file_Dictionary[listOfKmers[index]] + 1
#         else:
#             file_Dictionary[listOfKmers[index]] = 1

#     return file_Dictionary

# # --------------------------------------------------
# def Similarities(file1, file2):
#     """Find similarities and print the occurances"""

#     similarKmers = []
#     for key in file1:
#         if key in file2:
#             similarKmers.append(key)
#             if key in similarKmers:
#                 print(f'{key}{file1.get(key):10}{file2.get(key):5}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
