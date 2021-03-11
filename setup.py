#!/usr/bin/env python

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='ml4data',
      version='0.1',
      description='ML4Data client library',
      author='ML4Data Team',
      author_email='info@ml4data.com',
      url='https://ml4data.com/',
      packages=find_packages(),
      install_requires=required
     )
