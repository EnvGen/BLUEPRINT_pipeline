#!/usr/bin/env python
from setuptools import setup, find_packages
import sys, os
version = '0.1'

setup(name='BLUEPRINT_pipeline',
      version=version,
      description="The pipeline for running central BLUEPRINT bioinformatic analysis",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Python',
      author='Johannes Alneberg',
      author_email='johannes.alneberg@scilifelab.se',
      maintainer='Johannes Alneberg',
      maintainer_email='johannes.alneberg@scilifelab.se',
      url='https://github.com/EnvGen/BLUEPRINT_pipeline',
      scripts=['bin/bluepipe', 'scripts/rpkm_for_orfs.py'],
      packages=find_packages(exclude = ['examples', 'test']),
      zip_safe=False,
      install_requires=['nose'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

