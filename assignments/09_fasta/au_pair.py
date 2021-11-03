#!/usr/bin/env python3
"""
Author : caro <caro@localhost>
Date   : 2021-11-02
Purpose: Rock the Casbah
"""

import argparse
import os
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='au_pair.py 09_fasta assignment',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        nargs='+',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='input file(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        type=str,
                        metavar='DIR',
                        default='split')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    for fh in args.files:
        root, ext = os.path.splitext(os.path.basename(fh.name))
        forward = open(os.path.join(args.outdir, root + '_1' + ext), 'wt')
        reverse = open(os.path.join(args.outdir, root + '_2' + ext), 'wt')
        # print(fh.name, forward, reverse)
        parser = SeqIO.parse(fh, 'fasta')
        i = 0
        for rec in parser:
            is_even = i % 2 == 0
            # out_fh = forward if is_even else reverse
            # print(i, rec, id)
            i += 1
            SeqIO.write(rec, forward if is_even else reverse, 'fasta')

    print(f'Done, see output in "{args.outdir}"')
# --------------------------------------------------
if __name__ == '__main__':
    main()
