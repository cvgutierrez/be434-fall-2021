#!/usr/bin/env python3
"""
Author : root <root@localhost>
Date   : 2021-10-05
Purpose: Rock the Casbah
"""

import argparse
import pprint


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
                        default=None
                        )

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
    print('seq =', args.sequence)
    print('codons =', args.codons)
    print('outfile =', args.outfile)

    Dict = {}
    for line in args.codons:
    #   print(line.rstrip().split())
        KAI = line.rstrip().split()
        Dict[KAI[0]] = KAI[1]
    pp = pprint.PrettyPrinter() 
    #pp.pprint(Dict)

    k = 3
    seq = args.sequence
    translation = []
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        for key, value in Dict.items():
            if key == codon.upper():
                #print(codon.upper(), value)
                translation.append(value)
        #print(codon)
    print(''.join(translation), file=args.outfile)
    print(''.join(translation))



# --------------------------------------------------
if __name__ == '__main__':
    main()
