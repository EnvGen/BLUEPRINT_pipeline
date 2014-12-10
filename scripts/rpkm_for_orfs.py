#!/usr/bin/env python
"""rpkm_meta.py 

A script to calculate RPKM (number of reads per kilobase in 
reference and million reads in total) for each open reading frame (ORF). 

Using a gff file for defining the ORFs on contigs and a Bam mapping file 
where reads have been mapped against the contigs.
"""

import argparse
import sys
import pysam
import pandas as pd
import numpy as np
from BCBio import GFF

def main(args):
    samfile = pysam.AlignmentFile(args.bam_file, "rb")
    rpks = {}


    m_reads = float(args.n_reads) / 1e6
    for rec in GFF.parse(open(args.gff_file)):
        for feature in rec.features:
            feat_start = int(feature.location.start)
            feat_end = int(feature.location.end)
            feat_len = feat_end - feat_start + 1
            rpks[feature.id] = samfile.count(reference=rec.id, start=feat_start, end=feat_end) / (1e-3*feat_len*m_reads)

    s = pd.Series(rpks)
    s.to_csv(args.output_file, float_format="%.7f")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bam_file", help="Input BAM file.")
    parser.add_argument("gff_file", help="Input gff file.")
    parser.add_argument("n_reads", help="Number of reads used in mapping.")
    parser.add_argument('-o', '--output_file',
        help=("Optional output file where sequences will be printed." 
            " Otherwise use stdout."))

    args = parser.parse_args()

    main(args)
