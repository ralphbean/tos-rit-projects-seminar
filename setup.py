"""Setuptools setup file"""

import sys, os
import multiprocessing, logging

from setuptools import setup

setup(
    name='rit.floss',
    version='0.1',
    description="Materials for teaching open source at RIT",
    install_requires=[
        'Sphinx',
        'cloud_sptheme',
        'pyyaml',
        'feedparser',
    ],
    url = "http://teachingopensource.org/index.php/RIT",
    download_url = "https://github.com/ralphbean/tos-rit-projects-seminar",
    author='Ralph Bean',
    author_email='ralph.bean@gmail.com',
    license='GPLv3+',
    packages = [],
    namespace_packages = [],
    include_package_data=True,
    zip_safe=False,
    classifiers = [],
)
