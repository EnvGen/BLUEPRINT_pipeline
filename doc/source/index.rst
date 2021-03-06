.. BLUEPRINT Pipeline documentation master file, created by
   sphinx-quickstart on Wed Nov 26 09:09:17 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

BLUEPRINT Pipeline
==================
This documentation aim to cover the purpose and usage of a bioinformatics toolbox developed for the Blueprint project. 
Blueprint is a BONUS project and you can read more about it at the `Blueprint webpage`_ and about BONUS `here`_.

.. _Blueprint webpage: http://blueprint-project.org
.. _here: http://www.bonusportal.org

Purpose
-------
This toolbox or pipeline's aim is to be used to process metagenomic and metatranscriptomic sequencing data, produced by the Blueprint project, in order to present the results in a meaningful and comprehensive way.
The basis for the pipeline will be a reference metagenomic assembly, that will only be generated a few times.
Both metagenomic and metatranscriptomic samples will be mapped against the reference assembly to quantify the presence of each reference contig or reference open reading frame in the sample. 
When a new such assembly is performed all results derived from the assembly needs to be recomputed.

A big advantage in using a reference metagenomic assembly is that several computationally heavy steps, e.g. functional annotation and taxonomic classification, can be done once for the reference assembly and then reused for all samples.
As an example the taxonomic classification will be done per sequence in the reference assembly, and to estimate the abundance of a specific taxa in a sample, the pipeline looks at the all sequences classified as this taxa in the mapping of the sample sequences against the reference assembly. 

The outputs of the pipeline are files containing a quantitative measure for each gene or open reading frame in the reference assembly. Together with the annotation for the reference assembly, this is sufficient to quantify different annotations for each sample. 

As a quantification measure, RPKM, reads per kilobase per million reads, have been chosen since this normalizes the number of reads mapping to a gene with the length of the gene and the total number of reads in the sequencing output.

Contents:
=========
.. toctree::
   :maxdepth: 2

   usage
   implementation

