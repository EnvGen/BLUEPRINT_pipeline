Usage
=====
This section describes how to use the pipeline.
It is written assuming you are using a linux computer.
The pipeline extensively uses external software that needs to be installed before attempting to run the pipeline.
The software that needs to be installed is:

    - Bowtie2_
    - samtools_
    - Phylosift_
    - Fastqc_
    - Prokka_
    - Snakemake_
        
.. _Bowtie2: http://bowtie-bio.sourceforge.net/bowtie2/index.shtml
.. _Velvet: http://www.ebi.ac.uk/~zerbino/velvet/
.. _xclip: http://sourceforge.net/projects/xclip/
.. _parallel: https://www.gnu.org/software/parallel/
.. _samtools: http://samtools.sourceforge.net/
.. _CD-HIT: https://code.google.com/p/cdhit/
.. _AMOS: http://sourceforge.net/apps/mediawiki/amos/index.php?title=AMOS
.. _sickle: https://github.com/najoshi/sickle
.. _Picard: http://picard.sourceforge.net/index.shtml
.. _Ray: http://denovoassembler.sourceforge.net/
.. _Phylosift: http://phylosift.wordpress.com/
.. _Fastqc: http://www.bioinformatics.babraham.ac.uk/projects/fastqc/
.. _Sortmerna: http://bioinfo.lifl.fr/RNA/sortmerna/
.. _Rdp_Classifier: http://rdp.cme.msu.edu/
.. _Krona: http://sourceforge.net/p/krona/home/krona/
.. _Prokka: http://www.vicbioinformatics.com/software.prokka.shtml
.. _MinPath: http://omics.informatics.indiana.edu/MinPath/
.. _BedTools: http://bedtools.readthedocs.org/en/latest/
.. _Snakemake: https://bitbucket.org/johanneskoester/snakemake/wiki/Home

The pipeline itself should be downloaded from github::
    
    wget https://github.com/EnvGen/BLUEPRINT_pipeline/archive/master.zip
    unzip master.zip

    cd BLUEPRINT_pipeline-master    


