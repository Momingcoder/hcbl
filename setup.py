#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name = 'hcbl',
    version = '0.0.1',
    description = 'A plugin for Hachi to detect contacts.',
    author = 'MomingCoder',
    author_email = 'a398445075@gmail.com',
    url = 'https://github.com/guokr/Hachi',
    license = 'MIT',
    keywords = ['filter', 'Hachi', 'plugin', 'blacklist'],
    classifiers = ['Topic :: Text Processing'],
    packages = find_packages(),
    install_requires = [],
    platform = ['Windows', 'Linux', 'Mac'],
)
