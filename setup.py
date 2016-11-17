#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pycountries

from __future__ import with_statement

# To install the tune-mv-integration-python library, open a Terminal shell,
# then run this file by typing:
#
# python setup.py install
#

import sys
import re
from setuptools import setup

REQUIREMENTS = [
    req for req in open('requirements.txt')
    .read().split('\n')
    if req != ''
]

PACKAGES = [
    'pycountries'
]

CLASSIFIERS = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

with open('pycountries/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

if len(sys.argv) < 2 or sys.argv[1] == 'version':
    print(version)
    sys.exit()

setup(
    name='pycountries',
    version=version,
    description='Countries, country-codes, and continents.',
    author='TUNE',
    author_email='jefft@tune.com',
    url='https://github.com/TuneLab/pycountries',
    keywords=["country", "country-code", "continent", "ISO 3166-1", "alpha-2", "alpha-3"],
    install_requires=REQUIREMENTS,
    packages=PACKAGES,
    package_data={'': ['LICENSE', 'NOTICE'], 'pycountries': ['*.pem']},
    package_dir={'pycountries': 'pycountries'},
    include_package_data=True,
    license='MIT License',
    zip_safe=False,
    classifiers=CLASSIFIERS,
    long_description="""\
    Python country data derived from wikipedia.
    -------------------------------------------

    DESCRIPTION

    Python converstion function for countries, country-codes, and continents.

    See https://github.com/TuneLab/pycountries for
    more information.

    LICENSE TUNE Multiverse Countries Library is distributed under the
    MIT License"""
)
