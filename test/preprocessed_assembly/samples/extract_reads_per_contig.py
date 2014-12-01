#!/usr/bin/env python
"""Extract paired reads mapping to a specific region 
from a bam file using samtools and bamtools."""
import argparse
from subprocess import call

def main(args):
    for region in args.regions:
        call("samtools view -f 0x02 -h -b {1} {0} | bamtools convert -format fastq > {0}.paired.fastq".format(region, args.bamfile), shell=True)
        call("grep -A 3 --no-group-separator '^@.*/1$' {0}.paired.fastq > {0}.1.fastq".format(region), shell=True) 
        call("grep -A 3 --no-group-separator '^@.*/2$' {0}.paired.fastq > {0}.2.fastq".format(region), shell=True)  
        call("rm {0}.paired.fastq".format(region), shell=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('regions', nargs='*',
            help="The regions which reads will be extracted")
    parser.add_argument('--bamfile', default = "all_0322bt-smds.bam",
            help="The bamfile from where, the extractions will be.")
    args = parser.parse_args()
    main(args)
