#!/usr/bin/env python3
"""
Author : root <root@localhost>
Date   : 2021-10-05
Purpose: Rock the Casbah
"""

import argparse
#import pprint


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        type=str,
                        help='Sequence needing translation')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        required=True,
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # print('seq =', args.sequence)
    # print('codons =', args.codons)
    # print('outfile =', args.outfile)

    codon_table = {}
    for line in args.codons:
    #   print(line.rstrip().split())
        key, value = line.rstrip().split()
        codon_table[key] = value
    #pp = pprint.PrettyPrinter() 
    #pprint.pprint(codon_table)

    k = 3
    seq = args.sequence.upper()
    translation = []
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        translation.append(codon_table.get(codon))
    print(''.join(translation), file=args.outfile)
    print(f'Output written to "{args.outfile.name}".')



# --------------------------------------------------
if __name__ == '__main__':
    main()
