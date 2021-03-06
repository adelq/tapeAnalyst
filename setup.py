import os
import sys
from distutils.core import setup

requirements = open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).readlines()
setup(
    name = 'tapeAnalyst',
    version = '0.1',
    install_requires = requirements,
    author = 'Justin Fear',
    author_email = 'fearjm@nih.gov',
    description = 'A utility to analysze images from the Agilent Tapestation and generate a set of metrics.',
    packages=['tapeAnalyst'],
    package_dir={'tapeAnalyst': 'tapeAnalyst'},
    package_data={'tapeAnalyst': ['templates/*.html']},
    scripts = ['bin/analyzeTapeStationPng'],
)
