#!/usr/bin/env python
# coding: utf-8
#
#  Copyright (c) 2008—2015 Andy Mikhailenko and contributors
#
#  This file is part of django-autoslugged.
#
#  django-autoslugged is free software under terms of the GNU Lesser
#  General Public License version 3 (LGPLv3) as published by the Free
#  Software Foundation. See the file README for copying conditions.
#

import os

from setuptools import setup

from _version_helper import __version__

REPO_URL = "https://github.com/mbourqui/django-autoslugged/"

README = ''
for ext in ['md', 'rst']:
    try:
        with open(os.path.join(os.path.dirname(__file__), 'README.' + ext)) as readme:
            README = readme.read()
    except FileNotFoundError as fnfe:
        pass

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-autoslugged',
    version=__version__,
    packages=['autoslugged'],

    requires=['python (>= 2.7)', 'django (>= 1.7.10)'],
    # in case you want to use slugify() with support for transliteration:
    extras_require={
        'cyrillic': 'pytils >= 0.2',
        'translitcodec': 'translitcodec >= 0.3',
    },
    description='An automated slug field for Django.',
    long_description=README,
    author='Marc Bourqui',
    author_email='pypi.kemar@bourqui.org',
    url=REPO_URL,
    download_url=REPO_URL + 'releases/tag/v' + __version__,
    license='GNU Lesser General Public License (LGPL), Version 3',
    keywords='django field slug auto unique transliteration i18n',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: General',
    ],
)
