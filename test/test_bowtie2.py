import os
from nose.tools import assert_true
import subprocess

class TestBowtie2(object):
    def tearDown(self):
        os.chdir('../..')
        subprocess.call('rm -r test/preprocessed_assembly/mapping', shell=True)

    def test_bowtie2(self):
        """Run the bowtie2 part of the pipeline for the test data"""
        os.chdir("test/preprocessed_assembly")
        cmd = "snakemake "
        if os.getenv('TRAVIS'):
            cmd += "--config travis=true "
        cmd += "--debug test_bowtie"
        subprocess.call(cmd, shell=True)
        assert_true( os.path.isfile( "mapping/bowtie2/assembly_v1/120322/120322.bam" ))
