#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This library brings the updated configparser from Python 3.5 to Python 2.6-3.5."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import codecs
import os
import sys
from setuptools import setup, find_packages

readme_filename = os.path.join(os.path.dirname(__file__), 'README.rst')
with codecs.open(readme_filename, encoding='utf8') as ld_file:
    long_description = ld_file.read()

requirements = []

if sys.version_info[0] == 2:
    # bail on UTF-8 and enable `import configparser` for Python 2
    author = 'Shubham Chaudhary'
    modules = ['configparser2']
    if sys.version_info[1] < 7:
        requirements.append('ordereddict')
else:
    author = 'Shubham Chaudhary'
    modules = []

setup(
    name='configparser2',
    version='4.0.0',
    author=author,
    author_email='me@shubhamchaudhary.in',
    description=__doc__,
    long_description=long_description,
    url='http://docs.python.org/3/library/configparser.html',
    keywords='configparser configparser2 ini parsing conf cfg configuration file',
    platforms=['any'],
    license='MIT',
    py_modules=modules,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    namespace_packages=['backports'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
