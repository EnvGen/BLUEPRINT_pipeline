Usage
=====
This section describes how to install and use the pipeline.
It is written assuming you are using a linux computer but the same instructions should be valid on a Mac OSX computer as well.
The pipeline uses external software that needs to be installed before attempting to run the pipeline.
The software that needs to be available is:

    - Bowtie2_
    - samtools_
        
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


Setting up the python environment
---------------------------------
Unfortunately this pipeline needs to have two different python environments available, since it needs to have two different versions (2.7 and 3.4) of python available. This instructions will setup these two environments for you using miniconda from Continuum_. If you're already using miniconda or anaconda, you might want to edit the commands to suit your needs.

.. _Continuum: http://continuum.io/

First download and install miniconda in your home directory::

    cd ~
    wget http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh -O miniconda.sh
    chmod u+x miniconda.sh
    ./miniconda.sh -b

Now we are ready to create the two environments.::

    conda create -n BLUEPRINT_pipeline python=3.4
    conda create -n BLUEPRINT_pipeline_2.7 python=2.7

    source activate BLUEPRINT_pipeline_2.7
    conda install --yes pip numpy scipy pandas 
    pip install pysam
    source deactivate
    
    source activate BLUEPRINT_pipeline
    conda install pip snakemake
    source deactivate

This will create one environment named BLUEPRINT_pipeline which uses python version 3.4 and will be the main version of python used for the pipeline. The other environment BLUEPRINT_pipeline2.7 is used for a custom script that is used to quantify the open reading frames used as a part of the pipeline.

We're now ready to install the pipeline itself, starting off by downloading it from github::
    
    wget https://github.com/EnvGen/BLUEPRINT_pipeline/archive/master.zip
    unzip master.zip

    cd BLUEPRINT_pipeline-master    

If these commands are successful, you should now have everything ready to run the small test example below.

Running an example
------------------
With the pipeline source code, a small test data example is supplied. By running this example, we aim to show how the pipeline works in practice. First, let's move into the test directory::

    cd test

This directory currently contains a few files, the output of the excellent 'tree' command shows us::

    $ tree
    .
    ├── config.json
    ├── config_uppmax.json
    ├── Snakefile
    └── test_data
        ├── annotation
        │   └── reference
        │       └── assembly_v1.gff
        ├── references
        │   └── assembly_v1.fna
        └── samples
            ├── 120322_R1.fastq
            ├── 120322_R2.fastq
            ├── 120507_R1.fastq
            └── 120507_R2.fastq

    5 directories, 9 files 

The files within the test_data directory is the data that we'll use to kick off our pipeline, the Snakefile defines what result files we'd like to create and how to create them, the config.json file defines specific configurations we'll need (for this case where the python2 executable is available), and config_uppmax.json is a special config file needed only if we're running our test on any of the uppmax_ clusters.

.. _uppmax: http://www.uppmax.uu.se/  

We'll use the command `snakemake` to run our pipeline. The first command will execute a rule in the Snakefile that creates a directory structure that will suite the pipeline, and creates links to the test_data files needed::

    snakemake prepare

Lets have a look at what this command created::

    $ tree
    .
    ├── annotation
    │   └── reference
    │       └── assembly_v1.gff
    ├── config.json
    ├── config_uppmax.json
    ├── mapping
    ├── quantification
    ├── references
    │   └── assembly_v1.fna
    ├── rpkm_for_orfs.py -> ~/repos/BLUEPRINT_pipeline/test/../scripts/rpkm_for_orfs.py
    ├── samples
    │   ├── 120322_R1.fastq
    │   ├── 120322_R2.fastq
    │   ├── 120507_R1.fastq
    │   └── 120507_R2.fastq
    ├── Snakefile
    └── test_data
        ├── annotation
        │   └── reference
        │       └── assembly_v1.gff
        ├── references
        │   └── assembly_v1.fna
        └── samples
            ├── 120322_R1.fastq
            ├── 120322_R2.fastq
            ├── 120507_R1.fastq
            └── 120507_R2.fastq

    11 directories, 16 files

This shows us that the command has created a directory structure similar to the one present in the 'test_data' directory and copied the files present in test_data. It has also created two new directories named mapping and quantification where some output from the pipeline will be stored and created a link to the script `rpkm_for_orfs.py`. Now we should check what the pipeline would do if we executed it. By adding the `--dryrun` argument to snakemake, it will not execute any command but only show what it would do::

    snakemake --dryrun all_from_mapping

This should output a list of rules with input files and output files connected to them. After going through this list, running the complete pipeline should now be as simple as::

    snakemake all_from_mapping

If everything went alright you should now have have the following files::

        $ tree
    .
    ├── annotation
    │   └── reference
    │       └── assembly_v1.gff
    ├── config.json
    ├── config_uppmax.json
    ├── mapping
    │   └── bowtie2
    │       ├── assembly_v1
    │       │   ├── 120322
    │       │   │   ├── 120322.bam.log
    │       │   │   ├── 120322-s.bam
    │       │   │   └── 120322-s.bam.bai
    │       │   └── 120507
    │       │       ├── 120507.bam.log
    │       │       ├── 120507-s.bam
    │       │       └── 120507-s.bam.bai
    │       ├── assembly_v1.1.bt2
    │       ├── assembly_v1.2.bt2
    │       ├── assembly_v1.3.bt2
    │       ├── assembly_v1.4.bt2
    │       ├── assembly_v1.rev.1.bt2
    │       └── assembly_v1.rev.2.bt2
    ├── quantification
    │   └── assembly_v1
    │       └── orf
    │           ├── 120322
    │           │   └── 120322.rpkm
    │           └── 120507
    │               └── 120507.rpkm
    ├── references
    │   └── assembly_v1.fna
    ├── rpkm_for_orfs.py -> ~/repos/BLUEPRINT_pipeline/test/../scripts/rpkm_for_orfs.py
    ├── samples
    │   ├── 120322_R1.fastq
    │   ├── 120322_R2.fastq
    │   ├── 120507_R1.fastq
    │   └── 120507_R2.fastq
    ├── Snakefile
    └── test_data
        ├── annotation
        │   └── reference
        │       └── assembly_v1.gff
        ├── references
        │   └── assembly_v1.fna
        └── samples
            ├── 120322_R1.fastq
            ├── 120322_R2.fastq
            ├── 120507_R1.fastq
            └── 120507_R2.fastq

    19 directories, 30 files

Where the two files `120322.rpkm` and `120507.rpkm` are the most interesting ones. These should contain one row for each open reading fram found in the file `annotation/reference/assembly_v1.gff`. Each row would then contain the ORF id and a RPKM value. 
