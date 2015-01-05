__author__ = "Johannes Alneberg"
__license__ = "MIT"

WORKFLOW_DIR = os.getcwd()

import os
import sys
import shutil

# Chose config file based on if we're on uppmax or not
if 'SNIC_RESOURCE' in os.environ:
    configfile: "config_uppmax.json"
else:
    configfile: "config.json"

include: os.path.join(WORKFLOW_DIR, "rules/mapping/bowtie2.rules")
include: os.path.join(WORKFLOW_DIR, "rules/mapping/samfiles.rules")
include: os.path.join(WORKFLOW_DIR, "rules/quantification/rpkm.rules")
include: os.path.join(WORKFLOW_DIR, "rules/qc/sickle.rules")
include: os.path.join(WORKFLOW_DIR, "rules/qc/fastqc.rules")

# Make sure the scripts are available in working dir
script_dir = os.path.join(WORKFLOW_DIR, "scripts")
for script in os.listdir(script_dir):
    script_name = os.path.basename(script)
    if not shutil.which(script_name) and not os.path.exists(script_name):
        print("Script {0} not available, exiting.".format(os.path.basename(script)))
        sys.exit(-1)

rule quantify_all:
    input:
        expand("quantification/{assembly}/orf/{samples}/{samples}.rpkm",
            samples = ["120322", "120507"],
            assembly = "assembly_v1"),
