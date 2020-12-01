#!/usr/bin/env python
# -*- coding: utf-8 -*

import os

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

with open('README.md', 'r', encoding='utf-8') as rm_file:
    readme = rm_file.read()

with open('HISTORY.md', 'r', encoding='utf-8') as hist_file:
    history = hist_file.read()

setup(
    name='umls-api',
    version='0.1.0',
    packages=find_packages('src', exclude=('tests',)),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    description='',
    author='O\'Dwyer Software',
    author_email='hello@odwyer.software',
    url='https://github.com/odwyersoftware/umls-api',
    license='Apache 2',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    install_requires=install_requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
